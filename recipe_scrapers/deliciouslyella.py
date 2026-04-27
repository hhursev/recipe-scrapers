from ._abstract import AbstractScraper


class DeliciouslyElla(AbstractScraper):
    @classmethod
    def host(cls):
        return "deliciouslyella.com"
