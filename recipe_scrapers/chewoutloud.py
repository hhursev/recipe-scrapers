from ._abstract import AbstractScraper


class ChewOutLoud(AbstractScraper):
    @classmethod
    def host(cls):
        return "chewoutloud.com"
