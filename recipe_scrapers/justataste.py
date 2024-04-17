# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class JustATaste(AbstractScraper):
    @classmethod
    def host(cls):
        return "justataste.com"

    def ratings(self):
        return self.schema.ratings()
