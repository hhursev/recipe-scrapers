from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class TastefullyGrace(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "tastefullygrace.com"
