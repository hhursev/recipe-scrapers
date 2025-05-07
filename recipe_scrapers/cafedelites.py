from ._abstract import AbstractScraper


class CafeDelites(AbstractScraper):
    @classmethod
    def host(cls):
        return "cafedelites.com"
