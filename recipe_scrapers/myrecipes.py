# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class MyRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "myrecipes.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()
