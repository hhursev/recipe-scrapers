from ._abstract import AbstractScraper


class Recept(AbstractScraper):
    @classmethod
    def host(cls):
        return "recept.se"
