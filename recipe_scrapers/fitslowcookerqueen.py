# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class FitSlowCookerQueen(AbstractScraper):
    @classmethod
    def host(cls):
        return "fitslowcookerqueen.com"

    def category(self):
        return self.schema.category()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".tasty-recipes-ingredients h4",
            ".tasty-recipes-ingredients ul li",
        )

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
