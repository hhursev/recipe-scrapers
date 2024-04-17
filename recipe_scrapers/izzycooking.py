# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class IzzyCooking(AbstractScraper):
    @classmethod
    def host(cls):
        return "izzycooking.com"

    def category(self):
        return self.schema.category()
