from ._abstract import AbstractScraper


class JustALittleBitOfBacon(AbstractScraper):
    @classmethod
    def host(cls):
        return "justalittlebitofbacon.com"
