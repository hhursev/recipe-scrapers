from ._abstract import AbstractScraper


class ZenBelly(AbstractScraper):
    @classmethod
    def host(cls):
        return "zenbelly.com"
