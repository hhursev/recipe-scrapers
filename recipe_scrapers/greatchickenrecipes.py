from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class greatchickenrecipes(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "greatchickenrecipes.com"
    
