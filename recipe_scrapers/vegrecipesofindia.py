from ._abstract import AbstractScraper


class VegRecipesOfIndia(AbstractScraper):
    @classmethod
    def host(cls):
        return "vegrecipesofindia.com"
