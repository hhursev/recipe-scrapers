# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class G750g(AbstractScraper):
    @classmethod
    def host(cls):
        return "750g.com"

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()
