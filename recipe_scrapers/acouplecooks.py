# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class ACoupleCooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "acouplecooks.com"

    def yields(self):
        return self.schema.yields()

    def instructions(self):
        return self.schema.instructions()
