# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class AmbitiousKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "ambitiouskitchen.com"

    def ratings(self):
        return self.schema.ratings()
