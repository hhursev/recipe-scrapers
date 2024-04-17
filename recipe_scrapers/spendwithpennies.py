# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class SpendWithPennies(AbstractScraper):
    @classmethod
    def host(cls):
        return "spendwithpennies.com"

    def ratings(self):
        return self.schema.ratings()
