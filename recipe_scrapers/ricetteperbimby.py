# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class RicettePerBimby(AbstractScraper):
    @classmethod
    def host(cls):
        return "ricetteperbimby.it"

    def category(self):
        return self.schema.category()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ricetta-ingredienti .label",
            ".ricetta-ingredienti .ingrediente",
        )

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
