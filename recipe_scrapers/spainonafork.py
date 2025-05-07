from ._abstract import AbstractScraper


class SpainOnAFork(AbstractScraper):
    @classmethod
    def host(cls):
        return "spainonafork.com"
