from ._abstract import AbstractScraper


class LeitesCulinaria(AbstractScraper):
    @classmethod
    def host(cls):
        return "leitesculinaria.com"
