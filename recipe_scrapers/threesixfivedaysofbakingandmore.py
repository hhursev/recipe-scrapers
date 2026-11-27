from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class ThreeSixFiveDaysOfBakingAndMore(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "365daysofbakingandmore.com"
