# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class ChefSavvy(AbstractScraper):
    @classmethod
    def host(cls):
        return "chefsavvy.com"

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
