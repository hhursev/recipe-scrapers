from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import normalize_string


class TheSpruceEats(AbstractScraper):
    @classmethod
    def host(cls):
        return "thespruceeats.com"

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.find("ul", {"class": "ingredient-list"}).find_all(
            "li", {"class": "simple-list__item"}
        )

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.find(
            "section", {"class": "section--instructions"}
        ).find_all("li")

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
