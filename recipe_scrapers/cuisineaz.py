# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class CuisineAZ(AbstractScraper):
    @classmethod
    def host(cls):
        return "cuisineaz.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients_list = self.schema.ingredients()

        # Check if the first line is blank and skip it
        if ingredients_list and not ingredients_list[0].strip():
            return ingredients_list[1:]

        return ingredients_list

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()
