from ._abstract import AbstractScraper


class FifteenSpatulas(AbstractScraper):
    @classmethod
    def host(cls):
        return "fifteenspatulas.com"
