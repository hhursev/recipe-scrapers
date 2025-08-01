from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class BowlOfDelicious(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "bowlofdelicious.com"
