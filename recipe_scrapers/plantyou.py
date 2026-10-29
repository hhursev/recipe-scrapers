from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class PlantYou(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "plantyou.com"
