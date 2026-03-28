from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class manusmenu(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "manusmenu.com"
    
