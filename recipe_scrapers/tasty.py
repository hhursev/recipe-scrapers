from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class Tasty(AbstractScraper):
    @classmethod
    def host(cls):
        return "tasty.co"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(), self.soup, ".ingredient-section-name", ".ingredient"
        )
