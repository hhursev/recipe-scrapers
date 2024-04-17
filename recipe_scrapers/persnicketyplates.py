# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class PersnicketyPlates(AbstractScraper):
    @classmethod
    def host(cls):
        return "persnicketyplates.com"

    def category(self):
        return self.schema.category()

    def cuisine(self):
        return self.schema.cuisine()
