from ._abstract import AbstractScraper


class PilipinasRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "pilipinasrecipes.com"
