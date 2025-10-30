from ._abstract import AbstractScraper


class FoodByMaria(AbstractScraper):
    @classmethod
    def host(cls):
        return "foodbymaria.com"
