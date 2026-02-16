from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class ohmyfoodrecipes(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "ohmyfoodrecipes.com"
    
