# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class TheCleverCarrot(AbstractScraper):
    @classmethod
    def host(cls):
        return "theclevercarrot.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".tasty-recipes-ingredients-body h4",
            ".tasty-recipes-ingredients-body li",
        )

    def ratings(self):
        return self.schema.ratings()
