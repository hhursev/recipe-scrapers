# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Kochbar(AbstractScraper):
    @classmethod
    def host(cls):
        return "kochbar.de"

    def description(self):
        return self.schema.description()

    def yields(self):
        return self.schema.yields()
