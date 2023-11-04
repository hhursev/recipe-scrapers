# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class FineDiningLovers(AbstractScraper):
    @classmethod
    def host(cls):
        return "finedininglovers.com"

    def title(self):
        return self.schema.title()

    def author(self):
        return self.schema.author()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def image(self):
        return self.schema.image()
