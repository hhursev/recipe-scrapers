# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class ErrensKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "errenskitchen.com"

    def category(self):
        return self.schema.category()
