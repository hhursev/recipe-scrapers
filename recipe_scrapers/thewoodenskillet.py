from ._abstract import AbstractScraper


class TheWoodenSkillet(AbstractScraper):
    @classmethod
    def host(cls):
        return "thewoodenskillet.com"
