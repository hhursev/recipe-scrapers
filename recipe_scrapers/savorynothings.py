from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class SavoryNothings(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "savorynothings.com"
