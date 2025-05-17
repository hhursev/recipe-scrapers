from ._abstract import AbstractScraper


class TastyOven(AbstractScraper):
    @classmethod
    def host(cls):
        return "tastyoven.com"
