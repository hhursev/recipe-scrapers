# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class WatchWhatUEat(AbstractScraper):
    @classmethod
    def host(cls):
        return "watchwhatueat.com"

    def ratings(self):
        return self.schema.ratings()
