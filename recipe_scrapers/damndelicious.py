from ._abstract import AbstractScraper


class DamnDelicious(AbstractScraper):
    @classmethod
    def host(cls):
        return "damndelicious.net"
