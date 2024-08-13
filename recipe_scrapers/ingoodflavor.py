from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class InGoodFlavor(AbstractScraper):
    @classmethod
    def host(cls):
        return "ingoodflavor.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".dr-title",
            ".dr-ingredient-name",
        )
