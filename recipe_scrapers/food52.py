from typing import List, Optional

from recipe_scrapers._abstract import AbstractScraper
from recipe_scrapers._utils import get_minutes, normalize_string


class Food52(AbstractScraper):
    @classmethod
    def host(cls):
        return "food52.com"

    def title(self) -> Optional[str]:
        print("title was called")
        return self.schema.title()

    def total_time(self) -> Optional[int]:
        ul = self.soup.find("ul", {"class": "recipe__details"})
        total = 0
        for li in ul.find_all("li"):
            if li.span.get_text().lower() in ["prep time", "cook time"]:
                total += get_minutes(list(li.children)[2].strip())
        return total

    def yields(self) -> Optional[str]:
        return self.schema.yields()

    def image(self) -> Optional[str]:
        return self.schema.image()

    def ingredients(self) -> Optional[List[str]]:
        return self.schema.ingredients()

    def instructions(self) -> Optional[str]:
        instructions = self.soup.findAll("li", {"class": "recipe__list-step"})

        return "\n".join(
            [
                normalize_string(instruction.span.get_text())
                for instruction in instructions
            ]
        )

    def ratings(self) -> Optional[float]:
        return self.schema.ratings()
