from ._abstract import AbstractScraper


class LoveAndLemons(AbstractScraper):
    @classmethod
    def host(cls):
        return "loveandlemons.com"
