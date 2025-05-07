from ._abstract import AbstractScraper


class Rewe(AbstractScraper):
    @classmethod
    def host(cls):
        return "rewe.de"
