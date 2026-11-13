from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class FancifulEats(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "fancifuleats.com"
