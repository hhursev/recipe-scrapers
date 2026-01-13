from ._abstract import AbstractScraper


class LittleSpoonFarm(AbstractScraper):
    @classmethod
    def host(cls):
        return "littlespoonfarm.com"
