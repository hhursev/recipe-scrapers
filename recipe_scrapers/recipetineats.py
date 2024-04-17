# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class RecipeTinEats(AbstractScraper):
    @classmethod
    def host(cls):
        return "recipetineats.com"

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()
