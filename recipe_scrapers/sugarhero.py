from ._abstract import AbstractScraper


class SugarHero(AbstractScraper):
    @classmethod
    def host(cls):
        return "sugarhero.com"
