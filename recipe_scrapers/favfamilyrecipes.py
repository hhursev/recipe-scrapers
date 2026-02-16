from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class favfamilyrecipes(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "favfamilyrecipes.com"
    
