from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class SpendWithPennies(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "spendwithpennies.com"
