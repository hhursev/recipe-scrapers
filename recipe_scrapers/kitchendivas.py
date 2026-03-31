from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class KitchenDivas(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "kitchendivas.com"
