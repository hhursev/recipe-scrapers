from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class FeelGoodFoodie(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "feelgoodfoodie.net"
