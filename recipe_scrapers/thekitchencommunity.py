# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class TheKitchenCommunity(AbstractScraper):
    @classmethod
    def host(cls):
        return "thekitchencommunity.org"

    def category(self):
        return self.schema.category()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
