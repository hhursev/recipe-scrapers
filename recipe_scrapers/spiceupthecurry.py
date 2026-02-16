from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class spiceupthecurry(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "spiceupthecurry.com"
    
