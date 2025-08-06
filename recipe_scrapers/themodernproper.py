from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml
from ._grouping_utils import group_ingredients


class TheModernProper(AbstractScraper):
    @classmethod
    def host(cls):
        return "themodernproper.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".recipe-ingredients__list-title",
            ".recipe-ingredients__item",
        )

    def nutrients(self):
        container = self.schema.nutrients()
        if not container:
            raise ElementNotFoundInHtml("Could not find nutritional info container")

        results = {}
        nutrient_mapping = {
            "calories": "calories",
            "fatContent": "fat",
            "saturatedFatContent": "saturated fat",
            "carbohydrateContent": "carbohydrates",
            "sugarContent": "sugar",
            "proteinContent": "protein",
            "sodiumContent": "sodium",
            "fiberContent": "fiber",
            "cholesterolContent": "cholesterol",
        }

        for key, value in container.items():
            if key not in nutrient_mapping:
                continue
            redundant_suffix = nutrient_mapping[key]
            if value.endswith(redundant_suffix):
                results[key] = value.removesuffix(redundant_suffix).strip()

        return results
