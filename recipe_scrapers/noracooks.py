from ._abstract import AbstractScraper


class NoraCooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "noracooks.com"
