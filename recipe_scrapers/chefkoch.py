# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Chefkoch(AbstractScraper):
    @classmethod
    def host(cls):
        return "chefkoch.de"

    def title(self):
        return self.schema.title()

    def description(self):
        return self.schema.description()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def total_time(self):
        return self.schema.total_time()

    def cook_time(self):
        return self.schema.cook_time()

    def prep_time(self):
        return self.schema.prep_time()
