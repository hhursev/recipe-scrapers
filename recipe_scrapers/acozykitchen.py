from ._abstract import AbstractScraper


class ACozyKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "acozykitchen.com"
