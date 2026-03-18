from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class BillyParisi(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "billyparisi.com"
