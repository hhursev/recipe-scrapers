from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class ForkToSpoon(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "forktospoon.com"
