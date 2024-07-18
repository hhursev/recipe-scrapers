from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class AllTheHealthyThings(AbstractScraper):
    @classmethod
    def host(cls):
        return "allthehealthythings.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".tasty-recipes-ingredients-body strong",
            ".tasty-recipes-ingredients-body li",
        )
