# southernliving.com scraper
# Written by G.D. Wallters
# Freely released the code to recipe_scraper group
# 9 February, 2020
# =======================================================

from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class SouthernLiving(AbstractScraper):
    @classmethod
    def host(cls):
        return "southernliving.com"

    def title(self) -> Optional[str]:
        return self.schema.title()

    def total_time(self) -> Optional[int]:
        return get_minutes(self.schema.total_time())

    def yields(self) -> Optional[str]:
        return get_yields(self.schema.yields())

    def image(self) -> Optional[str]:
        return self.schema.image()

    def ingredients(self) -> Optional[List[str]]:
        return self.schema.ingredients()

    def instructions(self) -> Optional[str]:
        instructions = self.soup.find("ul", {"class": "instructions-section"}).findAll(
            "li", {"class": "instructions-section-item"}
        )
        return "\n".join(
            [
                normalize_string(
                    instruction.find("div", {"class": "paragraph"}).get_text()
                )
                for instruction in instructions
            ]
        )

    def ratings(self) -> Optional[float]:
        return self.schema.ratings()

    def description(self):
        des = self.soup.find(
            "div",
            attrs={"class": lambda e: e.startswith("recipe-summary") if e else False},
        )
        return des
