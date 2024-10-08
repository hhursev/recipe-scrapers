from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class BarefootInThePines(AbstractScraper):
    @classmethod
    def host(cls):
        return "barefootinthepines.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".mv-create-ingredients h4",
            ".mv-create-ingredients ul li",
        )

    def nutrients(self):
        nutrition_section = self.soup.select_one(".mv-create-nutrition-box")
        if not nutrition_section:
            return None

        raw_nutrition_data = {
            item.select_one(".mv-create-nutrition-label")
            .get_text(strip=True)
            .lower()
            .rstrip(":"): item.get_text(strip=True)
            .replace(
                item.select_one(".mv-create-nutrition-label").get_text(strip=True), ""
            )
            .strip()
            for item in nutrition_section.select(".mv-create-nutrition-item")
            if item.select_one(".mv-create-nutrition-label")
        }

        nutrition_label_mapping = {
            "calories": "calories",
            "carbohydrates": "carbohydrateContent",
            "cholesterol": "cholesterolContent",
            "total fat": "fatContent",
            "fiber": "fiberContent",
            "protein": "proteinContent",
            "saturated fat": "saturatedFatContent",
            "serving size": "servingSize",
            "sodium": "sodiumContent",
            "sugar": "sugarContent",
            "trans fat": "transFatContent",
            "unsaturated fat": "unsaturatedFatContent",
        }

        standardized_nutrition_data = {
            nutrition_label_mapping[custom_label]: value
            for custom_label, value in raw_nutrition_data.items()
            if custom_label in nutrition_label_mapping
        }

        return standardized_nutrition_data
