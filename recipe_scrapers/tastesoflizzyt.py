from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class TastesOfLizzyT(AbstractScraper):
    @classmethod
    def host(cls):
        return "tastesoflizzyt.com"

    def title(self) -> Optional[str]:
        return self.soup.find("h2", {"class": "wprm-recipe-name"}).get_text()

    def total_time(self) -> Optional[int]:
        return get_minutes(
            self.soup.find("div", {"class": "wprm-recipe-total-time-container"})
        )

    def yields(self) -> Optional[str]:
        return get_yields(self.soup.find("span", {"class": "wprm-recipe-servings"}))

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.find(
            "ul", {"class": "wprm-recipe-ingredients"}
        ).findAll("li")

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.find(
            "ul", {"class": "wprm-recipe-instructions"}
        ).findAll("li")

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
