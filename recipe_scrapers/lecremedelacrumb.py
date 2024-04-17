# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class LeCremeDeLaCrumb(AbstractScraper):
    @classmethod
    def host(cls):
        return "lecremedelacrumb.com"

    def ratings(self):
        return self.schema.ratings()
