# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class MyKitchen101en(AbstractScraper):
    @classmethod
    def host(cls):
        return "mykitchen101en.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()
