# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class Arla(AbstractScraper):
    @classmethod
    def host(cls):
        return "arla.se"

    def category(self):
        return self.schema.category()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "div.u-mt--m > h5",
            "div.u-mt--m > table > tbody > tr",
        )

    def cuisine(self):
        return self.schema.cuisine()

    def nutrients(self):
        return self.schema.nutrients()
