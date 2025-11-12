from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class OurBestBites(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "ourbestbites.com"
