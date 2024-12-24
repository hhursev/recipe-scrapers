from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class ZenBelly(AbstractScraper):
    @classmethod
    def host(cls):
        return "zenbelly.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".tasty-recipes-ingredients-body p",
            ".tasty-recipes-ingredients-body ul li",
        )
