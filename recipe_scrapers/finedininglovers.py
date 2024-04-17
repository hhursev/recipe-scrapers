# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class FineDiningLovers(AbstractScraper):
    @classmethod
    def host(cls):
        return "finedininglovers.com"

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()
