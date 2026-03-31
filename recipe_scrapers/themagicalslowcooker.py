from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class TheMagicalSlowCooker(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "themagicalslowcooker.com"
