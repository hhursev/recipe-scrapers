from ._abstract import AbstractScraper


class Sunset(AbstractScraper):
    @classmethod
    def host(cls):
        return "sunset.com"
