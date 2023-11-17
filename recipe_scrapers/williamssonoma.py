# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class WilliamsSonoma(AbstractScraper):
    @classmethod
    def host(cls):
        return "williams-sonoma.com"

    def author(self):
        return "Williams Sonoma"

    def title(self):
        return self.schema.title()

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
            ".botLeft > h3",
            ".botLeft > ul > li",
        )

    def instructions(self):
        return self.schema.instructions()

    def cuisine(self):
        return self.schema.cuisine()
