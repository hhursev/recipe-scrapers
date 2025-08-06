from ._abstract import AbstractScraper


class InsanelyGoodRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "insanelygoodrecipes.com"
