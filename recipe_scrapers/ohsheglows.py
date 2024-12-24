from ._abstract import AbstractScraper


class OhSheGlows(AbstractScraper):
    @classmethod
    def host(cls):
        return "ohsheglows.com"
