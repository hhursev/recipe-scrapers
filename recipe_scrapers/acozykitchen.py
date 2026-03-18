from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class ACozyKitchen(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "acozykitchen.com"
