from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class CastIronSkilletCooking(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "castironskilletcooking.com"
