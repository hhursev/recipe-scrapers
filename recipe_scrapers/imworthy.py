# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class ImWorthy(AbstractScraper):
    @classmethod
    def host(cls):
        return "im-worthy.com"

    def category(self):
        return self.schema.category()

    def cuisine(self):
        return self.schema.cuisine()
