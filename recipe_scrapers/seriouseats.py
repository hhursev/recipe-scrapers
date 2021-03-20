from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class SeriousEats(AbstractScraper):
    @classmethod
    def host(cls):
        return "seriouseats.com"

    def title(self) -> Optional[str]:
        return self.soup.find("h1").get_text()

    def total_time(self) -> Optional[int]:
        return get_minutes(self.soup.findAll("span", {"class": "info"})[2])

    def yields(self) -> Optional[str]:
        return get_yields(self.soup.find("span", {"class": "info yield"}))

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.findAll("li", {"class": "ingredient"})
        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.findAll("li", {"class": "recipe-procedure"})

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def ratings(self) -> Optional[float]:
        rating = self.soup.find("meta", {"property": "og:rating"})
        rating = (
            round(float(rating["content"]), 2) if rating and rating["content"] else -1.0
        )
        return rating
