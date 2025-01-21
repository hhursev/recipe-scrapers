from ._abstract import AbstractScraper


class Lecker(AbstractScraper):
    @classmethod
    def host(cls):
        return "lecker.de"
