from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class BudgetBytes(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "budgetbytes.com"
