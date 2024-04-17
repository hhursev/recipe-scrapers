# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class ComidinhasDoChef(AbstractScraper):
    @classmethod
    def host(cls):
        return "comidinhasdochef.com"

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()
