# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class MotherThyme(AbstractScraper):
    @classmethod
    def host(cls):
        return "motherthyme.com"

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()
