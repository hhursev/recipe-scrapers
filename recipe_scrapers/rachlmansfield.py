from ._abstract import AbstractScraper
from ._utils import get_minutes


class RachlMansfield(AbstractScraper):
    @classmethod
    def host(cls):
        return "rachlmansfield.com"

    def total_time(self):
        # Total time is not reported correctly by the schema data. Using the sum of the prep and cook times
        # as a workaround instead.
        prep_time = get_minutes(self.schema.data.get("prepTime")) or 0
        cook_time = get_minutes(self.schema.data.get("cookTime")) or 0
        return prep_time + cook_time
