from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class Thinlicious(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "thinlicious.com"
