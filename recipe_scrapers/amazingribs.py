from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class AmazingRibs(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "amazingribs.com"
