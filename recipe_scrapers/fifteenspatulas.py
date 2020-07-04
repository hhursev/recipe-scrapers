from ._abstract import AbstractScraper


class FifteenSpatulas(AbstractScraper):
    @classmethod
    def host(self):
        return "fifteenspatulas.com"
