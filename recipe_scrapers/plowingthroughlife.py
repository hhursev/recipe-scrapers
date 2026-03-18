from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class PlowingThroughLife(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "plowingthroughlife.com"
