# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class AbuelasCounter(AbstractScraper):
    @classmethod
    def host(cls):
        return "abuelascounter.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredient-item-group-title",
            ".wpzoom-rcb-ingredient-name",
        )

    def instructions(self):
        return self.schema.instructions()

    def cuisine(self):
        return self.schema.cuisine()
