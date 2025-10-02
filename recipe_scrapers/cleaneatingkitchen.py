from ._abstract import AbstractScraper


class CleanEatingKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "cleaneatingkitchen.com"
