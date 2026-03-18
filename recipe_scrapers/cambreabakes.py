from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class CambreaBakes(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "cambreabakes.com"
