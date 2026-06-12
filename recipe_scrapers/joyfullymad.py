from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class JoyfullyMad(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "joyfullymad.com"
