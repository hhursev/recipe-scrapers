from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class SkinnyTaste(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "skinnytaste.com"
