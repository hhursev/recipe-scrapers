from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class BlessThisMessPlease(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "blessthismessplease.com"
