from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class WeDishItUp(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "wedishitup.com"
