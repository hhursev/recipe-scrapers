# mypy: allow-untyped-defs
from ._abstract import AbstractScraper


class EmmiKochtEinfach(AbstractScraper):
    @classmethod
    def host(cls):
        return "emmikochteinfach.de"

    def category(self):
        return self.schema.category()

    def cuisine(self):
        return self.schema.cuisine()
