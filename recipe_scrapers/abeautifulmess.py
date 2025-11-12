from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class ABeautifulMess(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "abeautifulmess.com"
