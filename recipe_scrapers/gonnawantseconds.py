# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class GonnaWantSeconds(AbstractScraper):
    @classmethod
    def host(cls):
        return "gonnawantseconds.com"

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def description(self):
        return self.schema.description()
