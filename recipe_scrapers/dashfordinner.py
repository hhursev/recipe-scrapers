from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class DashForDinner(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "dashfordinner.com"
