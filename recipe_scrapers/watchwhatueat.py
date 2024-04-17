# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class WatchWhatUEat(AbstractScraper):
    @classmethod
    def host(cls):
        return "watchwhatueat.com"

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()
