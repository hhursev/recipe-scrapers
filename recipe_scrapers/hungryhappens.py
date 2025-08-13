from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class HungryHappens(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "hungryhappens.net"
