# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._decorators import schemaorg_fallback


class CookEatShare(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookeatshare.com"

    def title(self):
        return self.schema.title()

    @schemaorg_fallback
    def author(self):
        pass

    def total_time(self):
        return None

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()
