# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class ChefSavvy(AbstractScraper):
    @classmethod
    def host(cls):
        return "chefsavvy.com"

    def category(self):
        return self.schema.category()

    def cuisine(self):
        return self.schema.cuisine()
