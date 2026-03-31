from ._abstract import AbstractScraper


class TheSaltyMarshmallow(AbstractScraper):
    @classmethod
    def host(cls):
        return "thesaltymarshmallow.com"
