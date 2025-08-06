from ._abstract import AbstractScraper


class EatTolerant(AbstractScraper):
    @classmethod
    def host(cls):
        return "eattolerant.de"
