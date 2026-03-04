from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class daringgourmet(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "daringgourmet.com"
    
