# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class PurpleCarrot(AbstractScraper):
    @classmethod
    def host(cls):
        return "purplecarrot.com"

    def yields(self):
        return self.schema.yields()

    def nutrients(self):
        return self.schema.nutrients()
