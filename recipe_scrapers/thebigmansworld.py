from ._abstract import AbstractScraper


class TheBigMansWorld(AbstractScraper):
    @classmethod
    def host(cls):
        return "thebigmansworld.com"
