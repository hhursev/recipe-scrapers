from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class BakeWithZoha(AbstractScraper):
    @classmethod
    def host(cls):
        return "bakewithzoha.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".tasty-recipes-ingredients p strong",
            ".tasty-recipes-ingredients li",
        )
