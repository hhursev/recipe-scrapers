# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class ClosetCooking(AbstractScraper):
    @classmethod
    def host(cls):
        return "closetcooking.com"

    def yields(self):
        return self.schema.yields()
