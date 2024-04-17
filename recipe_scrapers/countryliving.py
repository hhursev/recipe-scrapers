# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class CountryLiving(AbstractScraper):
    @classmethod
    def host(cls):
        return "countryliving.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()
