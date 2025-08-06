from ._abstract import AbstractScraper


class SimpleVeganista(AbstractScraper):
    @classmethod
    def host(cls):
        return "simple-veganista.com"
