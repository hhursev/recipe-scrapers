from ._abstract import AbstractScraper


class CorrieCooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "corriecooks.com"
