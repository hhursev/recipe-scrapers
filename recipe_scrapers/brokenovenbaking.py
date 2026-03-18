from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class BrokenOvenBaking(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "brokenovenbaking.com"
