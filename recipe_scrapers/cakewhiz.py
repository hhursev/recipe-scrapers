from ._abstract import AbstractScraper


class CakeWhiz(AbstractScraper):
    @classmethod
    def host(cls):
        return "cakewhiz.com"
