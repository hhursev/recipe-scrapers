from ._abstract import AbstractScraper


class AmbitiousKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "ambitiouskitchen.com"
