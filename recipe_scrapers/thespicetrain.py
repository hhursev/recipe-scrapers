from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class TheSpiceTrain(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "thespicetrain.com"
