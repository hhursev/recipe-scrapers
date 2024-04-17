# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class SouthernCastIron(AbstractScraper):
    @classmethod
    def host(cls, domain="southerncastiron.com"):
        return domain

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()
