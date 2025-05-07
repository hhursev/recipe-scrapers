from ._abstract import AbstractScraper


class TheMagicalSlowCooker(AbstractScraper):
    @classmethod
    def host(cls):
        return "themagicalslowcooker.com"
