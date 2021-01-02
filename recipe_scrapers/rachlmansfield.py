from ._abstract import AbstractScraper
from ._utils import get_minutes


class RachlMansfield(AbstractScraper):
    @classmethod
    def host(cls):
        return "rachlmansfield.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        # Total time is not reported correctly by the schema data. Using the sum of the prep and cook times
        # as a workaround instead.
        prep_time = get_minutes(self.schema.data.get("prepTime")) or 0
        cook_time = get_minutes(self.schema.data.get("cookTime")) or 0
        return prep_time + cook_time

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
