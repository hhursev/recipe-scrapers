from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class TastesBetterFromScratch(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "tastesbetterfromscratch.com"
