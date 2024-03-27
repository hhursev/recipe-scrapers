# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class Template(AbstractScraper):
    @classmethod
    def host(cls):
        return "example.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def author(self):
        # question: should we make this a required field?
        return self.schema.author()

    def category(self):
        return self.schema.category()

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
