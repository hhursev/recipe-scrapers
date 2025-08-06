from ._abstract import AbstractScraper


class Ica(AbstractScraper):
    @classmethod
    def host(cls):
        return "ica.se"
