from ._abstract import AbstractScraper


class SudachiRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "sudachirecipes.com"
