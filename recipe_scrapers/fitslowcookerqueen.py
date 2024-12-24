from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class FitSlowCookerQueen(AbstractScraper):
    @classmethod
    def host(cls):
        return "fitslowcookerqueen.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".tasty-recipes-ingredients h4",
            ".tasty-recipes-ingredients ul li",
        )
