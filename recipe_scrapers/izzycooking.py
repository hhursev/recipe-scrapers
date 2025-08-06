from ._abstract import AbstractScraper


class IzzyCooking(AbstractScraper):
    @classmethod
    def host(cls):
        return "izzycooking.com"
