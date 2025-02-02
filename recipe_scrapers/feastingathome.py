from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class FeastingAtHome(AbstractScraper):
    @classmethod
    def host(cls):
        return "feastingathome.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".tasty-recipes-ingredients-body p strong",
            ".tasty-recipes-ingredients-body ul li",
        )
