from ._abstract import AbstractScraper


class Globo(AbstractScraper):
    @classmethod
    def host(cls):
        return "receitas.globo.com"
