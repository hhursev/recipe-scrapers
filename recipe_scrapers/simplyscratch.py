from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class SimplyScratch(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "simplyscratch.com"
