# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class TheKitchn(AbstractScraper):
    @classmethod
    def host(cls):
        return "thekitchn.com"

    def ratings(self):
        return self.schema.ratings()
