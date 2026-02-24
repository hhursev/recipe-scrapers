from ._abstract import AbstractScraper


class BarefeetInTheKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "barefeetinthekitchen.com"
