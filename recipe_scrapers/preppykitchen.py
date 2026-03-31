from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class PreppyKitchen(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "preppykitchen.com"
