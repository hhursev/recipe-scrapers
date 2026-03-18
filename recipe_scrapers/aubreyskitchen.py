from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class AubreysKitchen(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "aubreyskitchen.com"
