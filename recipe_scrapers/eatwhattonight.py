# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class EatWhatTonight(AbstractScraper):
    @classmethod
    def host(cls):
        return "eatwhattonight.com"

    def yields(self):
        return self.schema.yields()
