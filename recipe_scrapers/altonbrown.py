from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class AltonBrown(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "altonbrown.com"
