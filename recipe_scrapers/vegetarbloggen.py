# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class Vegetarbloggen(AbstractScraper):
    @classmethod
    def host(cls):
        return "vegetarbloggen.no"

    def category(self):
        return self.schema.category()

    def yields(self):
        return self.schema.yields()

    def instructions(self):
        return self.schema.instructions().strip()

    def description(self):
        return self.schema.description()
