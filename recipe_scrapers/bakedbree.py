from ._abstract import AbstractScraper


class BakedBree(AbstractScraper):
    @classmethod
    def host(cls):
        return "bakedbree.com"
