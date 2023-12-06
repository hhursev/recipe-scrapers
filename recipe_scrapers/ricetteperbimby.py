# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class RicettePerBimby(AbstractScraper):
    @classmethod
    def host(cls):
        return "ricetteperbimby.it"

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
            ".ricetta-ingredienti .label",
            ".ricetta-ingredienti .ingrediente",
        )

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
