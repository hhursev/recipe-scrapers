# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class TheExpertGuides(AbstractScraper):
    @classmethod
    def host(cls):
        return "theexpertguides.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def prep_time(self):
        return self.schema.prep_time()

    def cook_time(self):
        return self.schema.cook_time()

    def yields(self):
        return self.schema.yields()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
