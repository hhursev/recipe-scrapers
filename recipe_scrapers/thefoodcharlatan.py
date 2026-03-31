from ._abstract import AbstractScraper


class TheFoodCharlatan(AbstractScraper):
    @classmethod
    def host(cls):
        return "thefoodcharlatan.com"
