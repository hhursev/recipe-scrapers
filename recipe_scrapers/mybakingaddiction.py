from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class MyBakingAddiction(AbstractScraper):
    @classmethod
    def host(cls):
        return "mybakingaddiction.com"

    def title(self) -> Optional[str]:
        return self.soup.find("h1").get_text()

    def total_time(self) -> Optional[int]:
        return get_minutes(
            self.soup.find("div", {"class": "mv-create-time-total"}).get_text()
        )

    def yields(self) -> Optional[str]:
        return get_yields(self.soup.find("div", {"class": "mv-create-time-yield"}))

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.find("div", {"class": "mv-create-ingredients"}).findAll(
            "li"
        )

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.find(
            "div", {"class": "mv-create-instructions"}
        ).findAll("li")

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def ratings(self) -> Optional[float]:
        rating = self.soup.find("div", {"class": "mv-create-reviews"}).attrs.get(
            "data-mv-create-rating", None
        )

        return round(float(rating), 2)
