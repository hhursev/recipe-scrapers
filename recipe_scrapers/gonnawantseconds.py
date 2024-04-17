# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class GonnaWantSeconds(AbstractScraper):
    @classmethod
    def host(cls):
        return "gonnawantseconds.com"

    def yields(self):
        return self.schema.yields()

    def description(self):
        return self.schema.description()
