from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class TastyOven(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "tastyoven.com"
