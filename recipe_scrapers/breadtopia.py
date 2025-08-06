from ._abstract import AbstractScraper


class Breadtopia(AbstractScraper):
    @classmethod
    def host(cls):
        return "breadtopia.com"
