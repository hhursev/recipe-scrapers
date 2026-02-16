from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class liveeatlearn(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "liveeatlearn.com"
    
