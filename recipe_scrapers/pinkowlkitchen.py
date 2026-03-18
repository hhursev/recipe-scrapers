from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class PinkOwlKitchen(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "pinkowlkitchen.com"
