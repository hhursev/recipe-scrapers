from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class EatingOnADime(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "eatingonadime.com"
