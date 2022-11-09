# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class MotherThyme(AbstractScraper):
    @classmethod
    def host(cls):
        return "motherthyme.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()
