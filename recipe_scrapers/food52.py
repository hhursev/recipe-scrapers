# mypy: disallow_untyped_defs=False
from recipe_scrapers._abstract import AbstractScraper


class Food52(AbstractScraper):
    @classmethod
    def host(cls):
        return "food52.com"

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()
