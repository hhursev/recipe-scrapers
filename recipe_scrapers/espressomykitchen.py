from ._abstract import AbstractScraper
from ._wprm import WPRMMixin

class EspressoMyKitchen(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "espressomykitchen.com"
