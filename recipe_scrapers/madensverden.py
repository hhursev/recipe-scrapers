# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class MadensVerden(AbstractScraper):
    @classmethod
    def host(cls):
        return "madensverden.dk"

    def category(self):
        return self.schema.category()

    def nutrients(self):
        return self.schema.nutrients()

    def cuisine(self):
        return self.schema.cuisine()
