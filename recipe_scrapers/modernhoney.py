from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class ModernHoney(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "modernhoney.com"
