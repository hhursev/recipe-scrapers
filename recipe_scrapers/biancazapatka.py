from ._abstract import AbstractScraper


class BiancaZapatka(AbstractScraper):
    @classmethod
    def host(cls):
        return "biancazapatka.com"
