# mypy: disallow_untyped_defs=False
from recipe_scrapers._abstract import AbstractScraper


class Food52(AbstractScraper):
    @classmethod
    def host(cls):
        return "food52.com"

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

    def ratings(self):
        return self.schema.ratings()
