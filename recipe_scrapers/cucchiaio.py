# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Cucchiaio(AbstractScraper):
    @classmethod
    def host(cls):
        return "cucchiaio.it"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()
