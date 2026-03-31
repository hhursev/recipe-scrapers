from ._abstract import AbstractScraper


class NatashasKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "natashaskitchen.com"
