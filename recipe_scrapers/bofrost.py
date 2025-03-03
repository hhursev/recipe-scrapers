from ._abstract import AbstractScraper


class Bofrost(AbstractScraper):
    @classmethod
    def host(cls):
        return "bofrost.de"
