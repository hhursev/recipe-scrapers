from ._abstract import AbstractScraper


class EatWhatTonight(AbstractScraper):
    @classmethod
    def host(cls):
        return "eatwhattonight.com"
