# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Sunset(AbstractScraper):
    @classmethod
    def host(cls):
        return "sunset.com"

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()
