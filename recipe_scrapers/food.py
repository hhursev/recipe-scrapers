# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._decorators import opengraph_fallback, schemaorg_fallback


class Food(AbstractScraper):
    @classmethod
    def host(cls):
        return "food.com"

    def title(self):
        return self.schema.title()

    @schemaorg_fallback
    def author(self):
        pass

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    @opengraph_fallback
    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    @schemaorg_fallback
    def ratings(self):
        pass
