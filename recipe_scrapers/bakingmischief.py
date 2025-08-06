from ._abstract import AbstractScraper


class BakingMischief(AbstractScraper):
    @classmethod
    def host(cls):
        return "bakingmischief.com"
