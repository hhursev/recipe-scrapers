# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class SimpleVeganista(AbstractScraper):
    @classmethod
    def host(cls):
        return "simple-veganista.com"

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
