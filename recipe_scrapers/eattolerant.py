# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class EatTolerant(AbstractScraper):
    @classmethod
    def host(cls):
        return "eattolerant.de"

    def description(self):
        return self.schema.description()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()
