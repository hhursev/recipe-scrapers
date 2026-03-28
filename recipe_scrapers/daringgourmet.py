from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class DaringGourmet(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "daringgourmet.com"
