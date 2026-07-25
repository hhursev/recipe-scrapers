from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class Downshiftology(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "downshiftology.com"
