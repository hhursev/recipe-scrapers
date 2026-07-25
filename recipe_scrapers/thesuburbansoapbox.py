from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class TheSuburbanSoapBox(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "thesuburbansoapbox.com"
