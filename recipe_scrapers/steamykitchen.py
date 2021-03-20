from typing import List, Optional

from ._abstract import AbstractScraper


class SteamyKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "steamykitchen.com"

    def author(self) -> Optional[str]:
        return self.schema.author()

    def title(self) -> Optional[str]:
        return self.schema.title()

    def total_time(self) -> Optional[int]:
        return self.schema.total_time()

    def yields(self) -> Optional[str]:
        return self.schema.yields()

    def image(self) -> Optional[str]:
        # Recipe section and schema have no image so stealing from the page
        return self.soup.find("img")["src"]

    def ingredients(self) -> Optional[List[str]]:
        return self.schema.ingredients()

    def instructions(self) -> Optional[str]:
        return self.schema.instructions()

    def ratings(self) -> Optional[float]:
        # Schema has no ratings and I can't see any near the recipe
        return None
