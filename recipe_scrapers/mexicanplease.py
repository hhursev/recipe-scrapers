from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class mexicanplease(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "mexicanplease.com"
    
