from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class SavoryThoughts(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "savorythoughts.com"
