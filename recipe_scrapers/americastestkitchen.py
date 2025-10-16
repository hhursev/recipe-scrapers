from ._abstract import AbstractScraper


class AmericasTestKitchen(AbstractScraper):

    @classmethod
    def host(cls):
        return "americastestkitchen.com"
