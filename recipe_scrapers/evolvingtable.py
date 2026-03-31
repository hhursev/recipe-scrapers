from ._abstract import AbstractScraper


class EvolvingTable(AbstractScraper):
    @classmethod
    def host(cls):
        return "evolvingtable.com"
