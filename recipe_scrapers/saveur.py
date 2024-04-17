# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Saveur(AbstractScraper):
    @classmethod
    def host(cls):
        return "saveur.com"

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()
