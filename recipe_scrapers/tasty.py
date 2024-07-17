from ._abstract import AbstractScraper


class Tasty(AbstractScraper):
    @classmethod
    def host(cls):
        return "tasty.co"
