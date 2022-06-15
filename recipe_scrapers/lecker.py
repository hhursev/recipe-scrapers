from ._abstract import AbstractScraper
from ._exceptions import SchemaOrgException


class Lecker(AbstractScraper):
    @classmethod
    def host(cls):
        return "lecker.de"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def prep_time(self):
        return self.schema.prep_time()

    def cook_time(self):
        return self.schema.cook_time()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def nutrients(self):
        return self.schema.nutrients()

    def cuisine(self):
        try:
            return self.schema.cuisine()
        except SchemaOrgException:
            return None

    def description(self):
        return self.schema.description()
