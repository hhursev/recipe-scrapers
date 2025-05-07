from ._abstract import AbstractScraper


class Miljuschka(AbstractScraper):
    @classmethod
    def host(cls):
        return "miljuschka.nl"
