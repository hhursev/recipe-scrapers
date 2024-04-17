# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class WellPlated(AbstractScraper):
    @classmethod
    def host(cls):
        return "wellplated.com"

    def category(self):
        return self.schema.category()

    def cuisine(self):
        return self.schema.cuisine().replace(",", ", ")

    def description(self):
        return self.schema.description()
