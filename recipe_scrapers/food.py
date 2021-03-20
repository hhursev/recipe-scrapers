from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class Food(AbstractScraper):
    @classmethod
    def host(cls):
        return "food.com"

    def title(self) -> Optional[str]:
        return self.soup.find("h1").get_text()

    def total_time(self) -> Optional[int]:
        return get_minutes(self.soup.find("div", {"class": "recipe-facts__time"}))

    def yields(self) -> Optional[str]:
        return get_yields(
            self.soup.find("div", {"class": "recipe-facts__servings"}).get_text()
        )

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.findAll("li", {"class": "recipe-ingredients__item"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.findAll("li", {"class": "recipe-directions__step"})

        return "\n".join([instruction.get_text() for instruction in instructions])
