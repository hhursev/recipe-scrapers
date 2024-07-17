import re

import requests

from ._abstract import HEADERS, AbstractScraper
from ._exceptions import StaticValueException
from ._utils import get_yields

SCRIPT_PATTERN = re.compile(r'"recipeId":(\d+)')


class MonsieurCuisine(AbstractScraper):
    def __init__(self, url, proxies=None, timeout=None, *args, **kwargs):
        super().__init__(url=url, proxies=proxies, timeout=timeout, *args, **kwargs)
        recipe_id = None
        for script in self.soup.find_all("script"):
            matches = SCRIPT_PATTERN.search(str(script.string))
            if matches:
                recipe_id = matches.group(1)
        language_iso = self.language()
        data_url = f"https://mc-api.tecpal.com/api/v2/recipes/{recipe_id}"
        headers = HEADERS.copy()
        headers.update({"Accept-Language": language_iso, "Device-Type": "web"})
        self.data = requests.get(
            data_url,
            headers=headers,
            proxies=proxies,
            timeout=timeout,
        ).json()

    @classmethod
    def host(cls):
        return "monsieur-cuisine.com"

    def author(self):
        return self.data.get("data").get("recipe").get("author").get("name")

    def site_name(self):
        raise StaticValueException(return_value="Monsieur Cuisine")

    def cuisine(self):
        return None

    def category(self):
        categories = self.data.get("data").get("recipe").get("categories")
        return ", ".join([obj.get("name") for obj in categories])

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
        schema_mapping = {
            "Calories": "calories",
            "Carbohydrate": "carbohydrateContent",
            "Fat": "fatContent",
            "Protein": "proteinContent",
        }

        results = {}
        for nutrient in self.data.get("data").get("recipe").get("nutrients"):
            output_field = schema_mapping.get(nutrient.get("name"))
            if output_field is not None:
                results[output_field] = (
                    f'{nutrient.get("amount")} {nutrient.get("unit")}'
                )
        return results
