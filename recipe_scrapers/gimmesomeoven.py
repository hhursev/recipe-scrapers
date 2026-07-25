from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class GimmeSomeOven(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "gimmesomeoven.com"
