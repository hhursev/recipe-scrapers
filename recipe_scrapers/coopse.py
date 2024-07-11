import json
import re

import requests

from recipe_scrapers._grouping_utils import IngredientGroup

from ._abstract import AbstractScraper

SCRIPT_PATTERN = re.compile('"recipeId":"(?P<recipeId>[0-9]+)"')


class CoopSE(AbstractScraper):
    def __init__(self, url, proxies=None, timeout=None, *args, **kwargs):
        super().__init__(url=url, proxies=proxies, timeout=timeout, *args, **kwargs)
        scripts = self.soup.find_all("script")
        recipe_id = None
        for script in scripts:
            matches = SCRIPT_PATTERN.search(str(script.string))
            if matches:
                data = matches.groupdict()
                recipe_id = data["recipeId"]
        data_url = f"https://proxy.api.coop.se/external/recipe/recipes/{recipe_id}?api-version=v1"
        self.page_data = requests.get(
            data_url,
            proxies=proxies,
            timeout=timeout,
        ).content
        self.data = json.loads(self.page_data)

    @classmethod
    def host(cls):
        return "coop.se"

    def author(self):
        return "Coop Sverige"

    def title(self):
        return self.data["name"]

    def category(self):
        for c in self.data["categories"]:
            if len(c["categories"]) > 0:
                if c["categories"][0] == "Typ av rätt":
                    return c["categories"][1]
        return None

    def total_time(self):
        return int(self.data["totalTime"].replace(" minuter", ""))

    def yields(self):
        return self.data["numberOfServings"]

    def image(self):
        return self.data["imageUrl"]

    def ingredients(self):
        groups = self.ingredient_groups()
        ingredients = []
        for g in groups:
            ingredients.extend(g.ingredients)
        return ingredients

    def ingredient_groups(self):
        groups = []
        for p in self.data["recipePart"]:
            ingredients = []
            for i in p["ingredients"]:
                quantity = i["quantity"]
                if quantity.endswith(".0"):
                    quantity = quantity[:-2]
                unit = i["unit"]
                if unit:
                    unit = f" {unit}"
                pre_preparation = i["prePreparation"]
                if not pre_preparation == "":
                    pre_preparation = f" {pre_preparation}"
                name = i["name"]
                if not quantity == "1" and not pre_preparation == " riven":
                    name = i["ingredient"]["pluralName"]
                ingredients.append(
                    f"{quantity}{unit}{pre_preparation} {name}{i['postPreparation']}"
                )

            groups.append(IngredientGroup(purpose=p["name"], ingredients=ingredients))
        return groups

    def instructions(self):
        return "\n".join(
            list(
                filter(
                    lambda x: len(x) > 0,
                    re.sub(
                        r"(<p>|<h3>|</h3>)", "", self.data["cookingInstructions"]
                    ).split("</p>"),
                )
            )
        )

    def ratings(self):
        return self.data["avgRating"]

    def cuisine(self):
        return None

    def description(self):
        return self.data["preamble"] or None
