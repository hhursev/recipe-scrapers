from ._abstract import AbstractScraper


class EmilyBites(AbstractScraper):
    @classmethod
    def host(cls):
        return "emilybites.com"
