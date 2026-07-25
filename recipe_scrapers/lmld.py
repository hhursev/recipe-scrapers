from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class Lmld(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "lmld.org"
