from ._abstract import AbstractScraper
from ._utils import get_minutes
from ._grouping_utils import group_ingredients


class Kikkoman(AbstractScraper):
    @classmethod
    def host(cls):
        return "kikkoman.eu"

    def author(self):
        return self.soup.find("meta", {"name": "author"})["content"]

    def ingredients(self):
        ingredients = []
        ingredient_elements = self.soup.select(".bb-ingredients-calculator__ingredient")

        for el in ingredient_elements:
            amount_tag = el.select_one(".bb-ingredients-calculator__ingredient__amount")
            label_tag = el.select_one(".bb-ingredients-calculator__ingredient__label")

            amount = (
                amount_tag.get_text(strip=True).replace("\u202f", " ")
                if amount_tag
                else ""
            )
            label = (
                label_tag.get_text(strip=True).replace("\u202f", " ")
                if label_tag
                else ""
            )

            if amount or label:
                combined = f"{amount} {label}".strip()
                ingredients.append(combined)

        return ingredients

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup.select_one(".bb-ingredients-calculator__content"),
            ".bb-ingredients-calculator__ingredient__subtitle",
            ".bb-ingredients-calculator__ingredient",
        )

    def category(self):
        category_data = self.schema.category()
        cleaned_category = ", ".join(
            part.strip() for part in category_data.split(",") if part.strip()
        )
        return cleaned_category

    def nutrients(self):
        nutrients_data = self.schema.nutrients()
        calories = nutrients_data.get("calories", "")

        if calories == "calories":
            return {}

        if calories.endswith("calories"):
            nutrients_data["calories"] = calories.replace(" calories", "")

        return nutrients_data

    def _get_time(self, time_type):
        item = self.soup.select_one(
            f'.bb-recipe-detail__preparation-time__detailed-item--detail:-soup-contains("{time_type} time")'
        )
        value = item.find_previous_sibling("span").get_text(strip=True) if item else ""
        return get_minutes(value)

    def prep_time(self):
        return self._get_time("preparation")

    def cook_time(self):
        return self._get_time("cooking")
