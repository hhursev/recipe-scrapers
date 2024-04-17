# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class TheModernProper(AbstractScraper):
    @classmethod
    def host(cls):
        return "themodernproper.com"

    def category(self):
        return self.schema.category()

    def cuisine(self):
        return self.schema.cuisine()
