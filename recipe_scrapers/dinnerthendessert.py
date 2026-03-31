from ._abstract import AbstractScraper


class DinnerThenDessert(AbstractScraper):
    @classmethod
    def host(cls):
        return "dinnerthendessert.com"
