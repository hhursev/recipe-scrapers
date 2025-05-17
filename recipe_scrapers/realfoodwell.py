from ._abstract import AbstractScraper


class RealFoodWell(AbstractScraper):
    @classmethod
    def host(cls):
        return "realfoodwell.com"
