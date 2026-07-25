from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class SpicySouthernKitchen(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "spicysouthernkitchen.com"
