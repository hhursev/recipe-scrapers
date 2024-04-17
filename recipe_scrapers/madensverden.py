# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class MadensVerden(AbstractScraper):
    @classmethod
    def host(cls):
        return "madensverden.dk"

    def category(self):
        return self.schema.category()

    def cook_time(self):
        return self.schema.cook_time()

    def prep_time(self):
        return self.schema.prep_time()

    def yields(self):
        return self.schema.yields()

    def nutrients(self):
        return self.schema.nutrients()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
