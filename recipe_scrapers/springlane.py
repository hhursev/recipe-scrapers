# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Springlane(AbstractScraper):
    @classmethod
    def host(cls):
        return "springlane.de"

    def cuisine(self):
        return self.schema.cuisine()

    def cook_time(self):
        return self.schema.cook_time()

    def prep_time(self):
        return self.schema.prep_time()

    def nutrients(self):
        return self.schema.nutrients()
