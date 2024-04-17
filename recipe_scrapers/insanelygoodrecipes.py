# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class InsanelyGoodRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "insanelygoodrecipes.com"

    def category(self):
        return self.schema.category()
