from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class HouseOfYumm(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "houseofyumm.com"
