from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class MyKidsLickTheBowl(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "mykidslickthebowl.com"
