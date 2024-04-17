# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class ZenBelly(AbstractScraper):
    @classmethod
    def host(cls):
        return "zenbelly.com"

    def ratings(self):
        return self.schema.ratings()
