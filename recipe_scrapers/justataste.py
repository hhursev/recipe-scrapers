from ._abstract import AbstractScraper


class JustATaste(AbstractScraper):
    @classmethod
    def host(cls):
        return "justataste.com"
