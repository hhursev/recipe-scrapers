# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class CookPad(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookpad.com"

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()
