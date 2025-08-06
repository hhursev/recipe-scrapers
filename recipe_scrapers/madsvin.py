from ._abstract import AbstractScraper


class Madsvin(AbstractScraper):
    @classmethod
    def host(cls):
        return "madsvin.com"
