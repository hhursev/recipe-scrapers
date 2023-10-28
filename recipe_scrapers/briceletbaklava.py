# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class BricelEtBaklava(AbstractScraper):
    @classmethod
    def host(cls):
        return "briceletbaklava.ch"

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def instructions(self):
        return self.schema.instructions()

    def ingredients(self):
        return self.schema.ingredients()

    def description(self):
        return self.schema.description()

    def author(self):
        return self.schema.author()
