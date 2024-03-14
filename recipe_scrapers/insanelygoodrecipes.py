# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class InsanelyGoodRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "insanelygoodrecipes.com"

    def description(self):
        return self.schema.description()
