from ._abstract import AbstractScraper


class ACoupleCooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "acouplecooks.com"
