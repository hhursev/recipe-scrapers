from ._abstract import AbstractScraper


class Kochbar(AbstractScraper):
    @classmethod
    def host(cls):
        return "kochbar.de"
