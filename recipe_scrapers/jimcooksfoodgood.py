# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class JimCooksFoodGood(AbstractScraper):
    @classmethod
    def host(cls):
        return "jimcooksfoodgood.com"

    def ratings(self):
        return self.schema.ratings()
