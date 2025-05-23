from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class ErinLivesWhole(AbstractScraper):
    @classmethod
    def host(cls):
        return "erinliveswhole.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".tasty-recipes-ingredients p",
            ".tasty-recipes-ingredients li",
        )
