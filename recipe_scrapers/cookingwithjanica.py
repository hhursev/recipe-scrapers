from ._abstract import AbstractScraper


class CookingWithJanica(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookingwithjanica.com"
