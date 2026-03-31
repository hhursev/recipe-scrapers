from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class MelsKitchenCafe(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "melskitchencafe.com"
