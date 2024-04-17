# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class OneHundredOneCookBooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "101cookbooks.com"

    def nutrients(self):
        return self.schema.nutrients()
