from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class ThePioneerWoman(AbstractScraper):
    @classmethod
    def host(cls):
        return "thepioneerwoman.com"

    def title(self) -> Optional[str]:
        return self.soup.find("h3", {"class": "recipe-title"}).get_text()

    def total_time(self) -> Optional[int]:
        return sum(
            [
                get_minutes(dd)
                for dd in self.soup.find(
                    "div", {"class": "recipe-summary-time"}
                ).findAll("dd")
            ]
        )

    def yields(self) -> Optional[str]:
        return get_yields(self.soup.find("span", {"itemprop": "recipeYield"}))

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.find("ul", {"class": "list-ingredients"}).findAll("li")

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.findAll("div", {"class": "panel-body"})[-1]

        return normalize_string(instructions.get_text()).replace(".", ".\n")
