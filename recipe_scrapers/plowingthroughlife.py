from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class PlowingThroughLife(AbstractScraper):
    @classmethod
    def host(cls):
        return "plowingthroughlife.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredients li",
        )
