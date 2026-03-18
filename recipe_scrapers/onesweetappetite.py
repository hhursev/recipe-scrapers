from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class OneSweetAppetite(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "onesweetappetite.com"
