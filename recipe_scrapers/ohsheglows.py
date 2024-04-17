# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class OhSheGlows(AbstractScraper):
    @classmethod
    def host(cls):
        return "ohsheglows.com"

    def ratings(self):
        return self.schema.ratings()
