# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Marmiton(AbstractScraper):
    @classmethod
    def host(cls):
        return "marmiton.org"

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()
