# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class Inspiralized(AbstractScraper):
    @classmethod
    def host(cls):
        return "inspiralized.com"

    def title(self):
        return self.schema.title()

    def author(self):
        return self.schema.author()

    def total_time(self):
        return self.schema.total_time()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()
