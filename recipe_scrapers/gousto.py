# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


# TODO: Remove? Switching over to GoustoJson 2022-08-01
class Gousto(AbstractScraper):
    @classmethod
    def host(cls):
        return "gousto.co.uk"

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()
