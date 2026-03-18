from ._abstract import AbstractScraper


class TheAlmondEater(AbstractScraper):
    @classmethod
    def host(cls):
        return "thealmondeater.com"
