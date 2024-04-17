# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class CountryLiving(AbstractScraper):
    @classmethod
    def host(cls):
        return "countryliving.com"

    def yields(self):
        return self.schema.yields()
