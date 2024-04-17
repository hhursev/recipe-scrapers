# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Hostthetoast(AbstractScraper):
    @classmethod
    def host(cls):
        return "hostthetoast.com"

    def ratings(self):
        return self.schema.ratings()
