from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class spicecravings(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "spicecravings.com"
    
