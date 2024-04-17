# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Food(AbstractScraper):
    @classmethod
    def host(cls):
        return "food.com"

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()
