# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Marmiton(AbstractScraper):
    @classmethod
    def host(cls):
        return "marmiton.org"

    def ratings(self):
        return self.schema.ratings()
