from ._abstract import AbstractScraper


class VeganRicha(AbstractScraper):
    @classmethod
    def host(cls):
        return "veganricha.com"
