from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class AbuelasCounter(AbstractScraper):
    @classmethod
    def host(cls):
        return "abuelascounter.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredient-item-group-title",
            ".wpzoom-rcb-ingredient-name",
        )
