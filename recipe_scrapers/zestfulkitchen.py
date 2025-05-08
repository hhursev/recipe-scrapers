from ._abstract import AbstractScraper


class ZestfulKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "zestfulkitchen.com"
