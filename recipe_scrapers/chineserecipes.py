from ._abstract import AbstractScraper


class ChineseRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "chineserecipes.xyz"
