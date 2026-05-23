from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class EmilyBites(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "emilybites.com"
