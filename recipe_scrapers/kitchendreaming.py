from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class KitchenDreaming(AbstractScraper):
    @classmethod
    def host(cls):
        return "kitchendreaming.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group-name",
            ".wprm-recipe-ingredient",
        )
