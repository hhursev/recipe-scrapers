from ._abstract import AbstractScraper
from ._exceptions import FieldNotProvidedByWebsiteException


class PostPunkKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "theppk.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)

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

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
