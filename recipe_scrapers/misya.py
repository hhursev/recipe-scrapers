# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Misya(AbstractScraper):
    @classmethod
    def host(cls):
        return "misya.info"

    def ratings(self):
        return self.schema.ratings()
