# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Leukerecepten(AbstractScraper):
    @classmethod
    def host(cls):
        return "leukerecepten.nl"

    def category(self):
        return self.schema.category()

    def cuisine(self):
        return self.schema.cuisine()
