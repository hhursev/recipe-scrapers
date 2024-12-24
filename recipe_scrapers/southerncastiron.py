from ._abstract import AbstractScraper


class SouthernCastIron(AbstractScraper):
    @classmethod
    def host(cls, domain="southerncastiron.com"):
        return domain
