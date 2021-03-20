from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes


class RachlMansfield(AbstractScraper):
    @classmethod
    def host(cls):
        return "rachlmansfield.com"

    def author(self) -> Optional[str]:
        return self.schema.author()

    def title(self) -> Optional[str]:
        return self.schema.title()

    def total_time(self) -> Optional[int]:
        # Total time is not reported correctly by the schema data. Using the sum of the prep and cook times
        # as a workaround instead.
        prep_time = get_minutes(self.schema.data.get("prepTime")) or 0
        cook_time = get_minutes(self.schema.data.get("cookTime")) or 0
        return prep_time + cook_time

    def yields(self) -> Optional[str]:
        return self.schema.yields()

    def image(self) -> Optional[str]:
        return self.schema.image()

    def ingredients(self) -> Optional[List[str]]:
        return self.schema.ingredients()

    def instructions(self) -> Optional[str]:
        return self.schema.instructions()

    def ratings(self) -> Optional[float]:
        return self.schema.ratings()
