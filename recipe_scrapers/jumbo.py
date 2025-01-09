from ._abstract import AbstractScraper


class Jumbo(AbstractScraper):
    @classmethod
    def host(cls):
        return "jumbo.com"
