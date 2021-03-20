# copykat.py
# Written by G.D. Wallters
# Freely released the code to recipe_scraper group
# 8 February, 2020
# =======================================================

from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import normalize_string


class CopyKat(AbstractScraper):
    @classmethod
    def host(cls):
        return "copykat.com"

    def title(self) -> Optional[str]:
        return self.schema.title()

    def total_time(self) -> Optional[int]:
        return self.schema.total_time()

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

    def description(self):
        d = normalize_string(self.soup.find("span", {"style": "display: block;"}).text)

        return d if d else None
