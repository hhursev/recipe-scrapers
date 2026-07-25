from ._abstract import AbstractScraper


class BiggerBolderBaking(AbstractScraper):
    @classmethod
    def host(cls):
        return "biggerbolderbaking.com"
