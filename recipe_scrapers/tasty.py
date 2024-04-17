# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Tasty(AbstractScraper):
    @classmethod
    def host(cls):
        return "tasty.co"

    def title(self):
        return self.schema.title()

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()
