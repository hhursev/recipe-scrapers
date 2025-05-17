from ._abstract import AbstractScraper


class Thewoksoflife(AbstractScraper):
    @classmethod
    def host(cls):
        return "thewoksoflife.com"
