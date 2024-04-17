# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class SimpleVeganista(AbstractScraper):
    @classmethod
    def host(cls):
        return "simple-veganista.com"

    def category(self):
        return self.schema.category()

    def cuisine(self):
        return self.schema.cuisine()
