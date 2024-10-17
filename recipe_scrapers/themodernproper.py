from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml


class TheModernProper(AbstractScraper):
    @classmethod
    def host(cls):
        return "themodernproper.com"

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
            if key in nutrient_mapping:
                content = value.replace(nutrient_mapping[key], "").strip()
                results[key] = content

        return results
