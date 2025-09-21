from ._abstract import AbstractScraper


class SmallTownWoman(AbstractScraper):
    @classmethod
    def host(cls):
        return "smalltownwoman.com"
