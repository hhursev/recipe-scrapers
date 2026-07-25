from ._abstract import AbstractScraper


class BelleOfTheKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "belleofthekitchen.com"
