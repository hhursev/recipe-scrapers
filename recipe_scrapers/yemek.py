from ._abstract import AbstractScraper


class Yemek(AbstractScraper):
    @classmethod
    def host(cls):
        return "yemek.com"
