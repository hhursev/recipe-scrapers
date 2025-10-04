from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class EmmiKochtEinfach(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "emmikochteinfach.de"
