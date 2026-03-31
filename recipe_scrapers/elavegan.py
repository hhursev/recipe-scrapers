from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class ElaVegan(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "elavegan.com"
