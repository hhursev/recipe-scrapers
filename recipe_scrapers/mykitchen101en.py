from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class MyKitchen101en(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "mykitchen101en.com"
