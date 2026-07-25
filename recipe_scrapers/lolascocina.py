from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class LolasCocina(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "lolascocina.com"
