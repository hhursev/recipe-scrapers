from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class MakeItDairyFree(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "makeitdairyfree.com"
