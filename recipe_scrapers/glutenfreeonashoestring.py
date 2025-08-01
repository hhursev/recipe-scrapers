from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class GlutenFreeOnAShoeString(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "glutenfreeonashoestring.com"
