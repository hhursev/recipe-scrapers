from ._abstract import AbstractScraper


class NoSalty(AbstractScraper):
    @classmethod
    def host(cls):
        return "nosalty.hu"
