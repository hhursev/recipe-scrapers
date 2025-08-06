from ._abstract import AbstractScraper


class HeatherChristo(AbstractScraper):
    @classmethod
    def host(cls):
        return "heatherchristo.com"
