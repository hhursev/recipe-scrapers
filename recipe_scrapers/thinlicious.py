# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Thinlicious(AbstractScraper):
    @classmethod
    def host(cls):
        return "thinlicious.com"

    def ratings(self):
        return self.schema.ratings()
