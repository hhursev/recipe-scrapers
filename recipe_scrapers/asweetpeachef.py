from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class ASweetPeaChef(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "asweetpeachef.com"
