# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class InsanelyGoodRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "insanelygoodrecipes.com"

    def category(self):
        return self.schema.category()

    def ratings(self):
        return self.schema.ratings()

    def description(self):
        return self.schema.description()
