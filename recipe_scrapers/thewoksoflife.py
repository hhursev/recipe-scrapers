# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Thewoksoflife(AbstractScraper):
    @classmethod
    def host(cls):
        return "thewoksoflife.com"

    def description(self):
        return self.schema.description()

    def ratings(self):
        return self.schema.ratings()
