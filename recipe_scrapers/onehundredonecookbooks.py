from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class OneHundredOneCookBooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "101cookbooks.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".cb101-recipe-ingredient-group-name",
            ".cb101-recipe-ingredient",
        )
