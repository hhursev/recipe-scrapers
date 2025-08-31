from ._abstract import AbstractScraper


class CookedAndLoved(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookedandloved.com"
