# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class Breadtopia(AbstractScraper):
    @classmethod
    def host(cls):
        return "breadtopia.com"

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def description(self):
        return self.schema.description()
