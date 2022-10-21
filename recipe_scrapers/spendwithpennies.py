# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._decorators import opengraph_fallback, schemaorg_fallback


class SpendWithPennies(AbstractScraper):
    @classmethod
    def host(cls):
        return "spendwithpennies.com"

    def title(self):
        return self.schema.title()

    @schemaorg_fallback
    def author(self):
        if type(self.page_data) == bytes and b"Holly Nilsson" in self.page_data:
            return "Holly Nilsson"
        if type(self.page_data) == str and "Holly Nilsson" in self.page_data:
            return "Holly Nilsson"

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

    def ratings(self):
        return self.schema.ratings()
