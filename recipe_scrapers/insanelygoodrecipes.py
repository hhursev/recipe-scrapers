from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class InsanelyGoodRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "insanelygoodrecipes.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredient-item-group-title",
            ".ingredient-item:not(.ingredient-item-group)",
        )
