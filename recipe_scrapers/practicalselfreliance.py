# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class PracticalSelfReliance(AbstractScraper):
    @classmethod
    def host(cls, domain="practicalselfreliance.com"):
        return domain

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()
