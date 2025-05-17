from ._abstract import AbstractScraper


class TheMediterraneDish(AbstractScraper):
    @classmethod
    def host(cls):
        return "themediterraneandish.com"
