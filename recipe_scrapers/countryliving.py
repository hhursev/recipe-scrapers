from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class CountryLiving(AbstractScraper):
    @classmethod
    def host(cls):
        return "countryliving.com"

    def title(self) -> Optional[str]:
        return self.soup.find("h1", {"class": "content-hed recipe-hed"}).get_text()

    def total_time(self) -> Optional[int]:
        return get_minutes(
            self.soup.find("span", {"class": "total-time-amount"}).parent
        )

    def yields(self) -> Optional[str]:
        yields = self.soup.find(
            "div", {"class": "recipe-details-item yields"}
        ).get_text()

        return get_yields("{} servings".format(yields))

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.findAll("div", {"class": "ingredient-item"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.find("div", {"class": "direction-lists"}).find_all(
            "li"
        )

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
