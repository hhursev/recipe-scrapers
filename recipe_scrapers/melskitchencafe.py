# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class MelsKitchenCafe(AbstractScraper):
    @classmethod
    def host(cls):
        return "melskitchencafe.com"

    def ratings(self):
        return self.schema.ratings()
