from ._abstract import AbstractScraper


class BetterFoodGuru(AbstractScraper):
    @classmethod
    def host(cls):
        return "betterfoodguru.com"
