from ._abstract import AbstractScraper


class AllRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "allrecipes.com"
