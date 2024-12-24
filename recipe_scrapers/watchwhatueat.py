from ._abstract import AbstractScraper


class WatchWhatUEat(AbstractScraper):
    @classmethod
    def host(cls):
        return "watchwhatueat.com"
