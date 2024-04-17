# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class AbuelasCounter(AbstractScraper):
    @classmethod
    def host(cls):
        return "abuelascounter.com"

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredient-item-group-title",
            ".wpzoom-rcb-ingredient-name",
        )

    def cuisine(self):
        return self.schema.cuisine()
