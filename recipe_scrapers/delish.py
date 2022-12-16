# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Delish(AbstractScraper):
    @classmethod
    def host(cls):
        return "delish.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()
