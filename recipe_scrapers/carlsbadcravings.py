from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class CarlsBadCravings(AbstractScraper):
    @classmethod
    def host(cls):
        return "carlsbadcravings.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-group-name.wprm-recipe-ingredient-group-name.wprm-block-text-bold",
            ".wprm-recipe-ingredient",
        )
