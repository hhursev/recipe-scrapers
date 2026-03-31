from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class ScrummyLane(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "scrummylane.com"
