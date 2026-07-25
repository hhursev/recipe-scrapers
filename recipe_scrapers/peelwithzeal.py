from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class PeelWithZeal(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "peelwithzeal.com"
