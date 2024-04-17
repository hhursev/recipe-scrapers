# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class HandleTheHeat(AbstractScraper):
    @classmethod
    def host(cls, domain="handletheheat.com"):
        return domain

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()
