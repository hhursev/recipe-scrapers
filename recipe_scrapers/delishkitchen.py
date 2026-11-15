from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class DelishKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "delishkitchen.tv"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredient-group__header",
            ".ingredient",
        )
