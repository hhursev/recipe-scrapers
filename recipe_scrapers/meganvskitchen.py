from ._abstract import AbstractScraper


class MeganVsKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "meganvskitchen.com"
