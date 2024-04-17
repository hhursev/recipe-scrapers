# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Springlane(AbstractScraper):
    @classmethod
    def host(cls):
        return "springlane.de"

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def cuisine(self):
        return self.schema.cuisine()

    def total_time(self):
        return self.schema.total_time()

    def cook_time(self):
        return self.schema.cook_time()

    def prep_time(self):
        return self.schema.prep_time()

    def yields(self):
        return self.schema.yields()

    def nutrients(self):
        return self.schema.nutrients()
