from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class foragerchef(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "foragerchef.com"
    
