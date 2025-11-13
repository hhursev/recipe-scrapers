from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class GoodStuffRecipes(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "goodstuff.recipes"
