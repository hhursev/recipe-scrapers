from ._abstract import AbstractScraper


class MyriadRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "myriadrecipes.com"
