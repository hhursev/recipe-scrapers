# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Springlane(AbstractScraper):
    @classmethod
    def host(cls):
        return "springlane.de"

    def category(self):
        return self.schema.category()

    def cuisine(self):
        return self.schema.cuisine()

    def nutrients(self):
        return self.schema.nutrients()
