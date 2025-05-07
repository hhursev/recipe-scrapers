from ._abstract import AbstractScraper


class GarnishAndGlaze(AbstractScraper):
    @classmethod
    def host(cls):
        return "garnishandglaze.com"
