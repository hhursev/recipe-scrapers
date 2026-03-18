from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class HowToCook(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "howtocook.recipes"
