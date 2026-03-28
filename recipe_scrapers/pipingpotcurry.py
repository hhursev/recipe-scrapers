from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class pipingpotcurry(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "pipingpotcurry.com"
    
