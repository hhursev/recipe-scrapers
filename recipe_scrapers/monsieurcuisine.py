# mypy: disallow_untyped_defs=False
import re

import requests

from ._abstract import AbstractScraper
from ._utils import get_yields

SCRIPT_PATTERN = re.compile(r'"recipeId":(\d+)')


class MonsieurCuisine(AbstractScraper):
    def __init__(self, url, proxies=None, timeout=None, *args, **kwargs):
        super().__init__(url=url, proxies=proxies, timeout=timeout, *args, **kwargs)
        scripts = self.soup.find_all("script")
        recipe_id = None
        for script in scripts:
            matches = SCRIPT_PATTERN.search(str(script.string))
            if matches:
                recipe_id = matches.group(1)
        language_iso = self.soup.find("html")["lang"]
        data_url = f"https://mc-api.tecpal.com/api/v2/recipes/{recipe_id}"
        self.data = requests.get(
            data_url,
            headers={"Accept-Language": language_iso, "Device-Type": "web"},
            proxies=proxies,
            timeout=timeout,
        ).json()

    @classmethod
    def host(cls):
        return "monsieur-cuisine.com"

    def author(self):
        return self.data.get("data").get("recipe").get("author").get("name")

    def title(self):
        return self.data.get("data").get("recipe").get("name")

    def total_time(self):
        return self.data.get("data").get("recipe").get("duration")

    def cook_time(self):
        prepare_time = self.data.get("data").get("recipe").get("preparationDuration")
        total_time = self.data.get("data").get("recipe").get("duration")

        return total_time - prepare_time

    def prep_time(self):
        return self.data.get("data").get("recipe").get("preparationDuration")

    def yields(self):
        default_serving = self.data.get("data").get("recipe").get("servingSizes")[0]

        return get_yields(
            f"{default_serving.get('amount')} {default_serving.get('servingUnit')}"
        )

    def image(self):
        return self.data.get("data").get("recipe").get("thumbnail").get("landscape")

    def ingredients(self):
        ingredients = []
        raw_ingridients = (
            self.data.get("data")
            .get("recipe")
            .get("servingSizes")[0]
            .get("ingredients")
        )
        for raw_ingredient in raw_ingridients:
            ingredients.append(
                f"{raw_ingredient.get('amount')} {raw_ingredient.get('unit')} {raw_ingredient.get('name')}"
            )

        return ingredients

    def instructions(self):
        instruction = (
            self.data.get("data")
            .get("recipe")
            .get("servingSizes")[0]
            .get("instruction")
        )

        instruction = re.sub(r"(\r\n\r\n)|(\n\n)", "__DOUBLE_NEWLINE__", instruction)

        instruction = re.sub(r"(\r\n)|(\n)", " ", instruction)

        instruction = instruction.replace("__DOUBLE_NEWLINE__", "\n")

        return instruction

    def ratings(self):
        return self.data.get("data").get("recipe").get("rating")

    def nutrients(self):
        nutrients = self.data.get("data").get("recipe").get("nutrients")

        for nutrient in nutrients:
            if nutrient.get("name") == "Calories":
                calories = nutrient
            if nutrient.get("name") == "Carbohydrate":
                carbohydrates = nutrient
            if nutrient.get("name") == "Fat":
                fat = nutrient
            if nutrient.get("name") == "Protein":
                protein = nutrient

        return {
            "calories": f'{calories.get("amount")} {calories.get("unit")}',
            "fatContent": f'{fat.get("amount")} {fat.get("unit")}',
            "carbohydrateContent": f'{carbohydrates.get("amount")} {carbohydrates.get("unit")}',
            "proteinContent": f'{protein.get("amount")} {protein.get("unit")}',
        }
