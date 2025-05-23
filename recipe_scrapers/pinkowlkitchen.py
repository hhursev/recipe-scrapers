from ._abstract import AbstractScraper


class PinkOwlKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "pinkowlkitchen.com"
