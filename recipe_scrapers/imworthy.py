# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class ImWorthy(AbstractScraper):
    @classmethod
    def host(cls):
        return "im-worthy.com"

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
