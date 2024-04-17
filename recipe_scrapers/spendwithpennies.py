# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class SpendWithPennies(AbstractScraper):
    @classmethod
    def host(cls):
        return "spendwithpennies.com"

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()
