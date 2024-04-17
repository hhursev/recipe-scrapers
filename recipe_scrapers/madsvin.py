# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class Madsvin(AbstractScraper):
    @classmethod
    def host(cls):
        return "madsvin.com"

    def category(self):
        return self.schema.category()

    def ratings(self):
        return self.schema.ratings()

    def description(self):
        return self.schema.description()
