# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class ErrensKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "errenskitchen.com"

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
