from ._abstract import AbstractScraper


class ThreeSixFiveDaysOfBakingAndMore(AbstractScraper):
    @classmethod
    def host(cls):
        return "365daysofbakingandmore.com"
