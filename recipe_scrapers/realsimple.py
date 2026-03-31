from ._abstract import AbstractScraper


class RealSimple(AbstractScraper):
    @classmethod
    def host(cls):
        return "realsimple.com"
