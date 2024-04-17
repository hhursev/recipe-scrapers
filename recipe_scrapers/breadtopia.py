# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class Breadtopia(AbstractScraper):
    @classmethod
    def host(cls):
        return "breadtopia.com"

    def category(self):
        return self.schema.category()

    def yields(self):
        return self.schema.yields()

    def description(self):
        return self.schema.description()
