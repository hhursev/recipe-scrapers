# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Leukerecepten(AbstractScraper):
    @classmethod
    def host(cls):
        return "leukerecepten.nl"

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
