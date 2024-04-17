# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class WellPlated(AbstractScraper):
    @classmethod
    def host(cls):
        return "wellplated.com"

    def category(self):
        return self.schema.category()

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine().replace(",", ", ")

    def description(self):
        return self.schema.description()
