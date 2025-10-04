from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class ChewOutLoud(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "chewoutloud.com"
