from ._abstract import AbstractScraper


class CookingLSL(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookinglsl.com"
