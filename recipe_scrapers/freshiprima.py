from ._abstract import AbstractScraper


class FreshiPrima(AbstractScraper):
    @classmethod
    def host(cls):
        return "fresh.iprima.cz"
