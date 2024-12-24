from ._abstract import AbstractScraper


class HandleTheHeat(AbstractScraper):
    @classmethod
    def host(cls, domain="handletheheat.com"):
        return domain
