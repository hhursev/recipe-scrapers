from ._abstract import AbstractScraper


class HilahCooking(AbstractScraper):
    @classmethod
    def host(cls):
        return "hilahcooking.com"
