from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class TheCleverCarrot(AbstractScraper):
    @classmethod
    def host(cls):
        return "theclevercarrot.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".tasty-recipes-ingredients-body h4",
            ".tasty-recipes-ingredients-body li",
        )
