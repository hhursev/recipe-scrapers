# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class OneHundredOneCookBooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "101cookbooks.com"

    def cuisine(self):
        return self.schema.cuisine()

    def nutrients(self):
        return self.schema.nutrients()
