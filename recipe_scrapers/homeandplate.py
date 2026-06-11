from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class HomeAndPlate(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "homeandplate.com"
