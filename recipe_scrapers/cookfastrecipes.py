from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class CookFastRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookfastrecipes.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredients-list h4",
            ".ingredients-list .ingredient-item label",
        )
