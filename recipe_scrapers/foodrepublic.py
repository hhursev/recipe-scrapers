from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class FoodRepublic(AbstractScraper):
    @classmethod
    def host(cls):
        return "foodrepublic.com"

    def title(self) -> Optional[str]:
        return self.soup.find("h3", {"class": "recipe-title"}).get_text()

    def total_time(self) -> Optional[int]:
        return sum(
            [
                get_minutes(self.soup.find("li", {"class": "prep-time"})),
                get_minutes(self.soup.find("li", {"class": "cook-time"})),
            ]
        )

    def yields(self) -> Optional[str]:
        return get_yields(self.soup.find("span", {"itemprop": "recipeYield"}))

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.findAll("li", {"itemprop": "recipeIngredient"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.find("div", {"class": "directions"}).findAll("li")

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
