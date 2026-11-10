from ._abstract import AbstractScraper
from ._wprm import WPRMMixin

class CoffeeCopycat(WPRMMixin,AbstractScraper):
    @classmethod
    def host(cls):
        return "coffeecopycat.com"
