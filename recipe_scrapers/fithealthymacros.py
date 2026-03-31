from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class FitHealthyMacros(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "fithealthymacros.com"
