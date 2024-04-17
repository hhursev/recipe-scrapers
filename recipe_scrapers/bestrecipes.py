# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class BestRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "bestrecipes.com.au"

    def category(self):
        return self.schema.category()

    def cuisine(self):
        return self.schema.cuisine()

    def language(self):
        return "en-AU"
