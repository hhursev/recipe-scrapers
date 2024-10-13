import re

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class WomensWeeklyFood(AbstractScraper):
    @classmethod
    def host(cls):
        return "womensweeklyfood.com.au"

    def instructions(self):
        return re.sub(r"\d+\.\n", "", self.schema.instructions())

    def ingredients(self):
        ingredients_elements = self.soup.select(
            ".recipe-ingredients__item span[itemprop='ingredients']"
        )
        return [ingredient.get_text(strip=True) for ingredient in ingredients_elements]

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".recipe-ingredients__title",
            ".recipe-ingredients__item span[itemprop='ingredients']",
        )
