# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Yemek(AbstractScraper):
    @classmethod
    def host(cls):
        return "yemek.com"

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()
