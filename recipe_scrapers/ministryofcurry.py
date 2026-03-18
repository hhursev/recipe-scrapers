from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class MinistryOfCurry(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "ministryofcurry.com"
