from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class AddAPinch(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "addapinch.com"
