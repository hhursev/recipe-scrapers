# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class DavidLebovitz(AbstractScraper):
    @classmethod
    def host(cls):
        return "davidlebovitz.com"

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

    def description(self):
        return self.schema.description()
