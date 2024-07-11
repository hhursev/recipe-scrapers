from ._abstract import AbstractScraper


class Thinlicious(AbstractScraper):
    @classmethod
    def host(cls):
        return "thinlicious.com"
