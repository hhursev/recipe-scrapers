from ._abstract import AbstractScraper


class TheGuardian(AbstractScraper):
    @classmethod
    def host(cls):
        return "theguardian.com"
