# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class WholeFoods(AbstractScraper):
    @classmethod
    def host(cls, domain="com"):
        return f"wholefoodsmarket.{domain}"

    def ratings(self):
        return self.schema.ratings()
