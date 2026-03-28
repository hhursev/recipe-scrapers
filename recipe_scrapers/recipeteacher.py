from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class recipeteacher(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "recipeteacher.com"
    
