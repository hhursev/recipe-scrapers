from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class AFullLiving(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "afullliving.com"
