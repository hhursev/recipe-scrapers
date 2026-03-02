from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class GarlicAndZest(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "garlicandzest.com"
