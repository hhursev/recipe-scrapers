from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class HundredAndOneCookbooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "101cookbooks.com"

    def title(self) -> Optional[str]:
        return self.soup.find("h1").get_text()

    def total_time(self) -> Optional[int]:
        return get_minutes(
            self.soup.findAll("div", {"class": "wprm-recipe-time"})[-1].get_text()
        )

    def yields(self) -> Optional[str]:
        return get_yields(
            self.soup.findAll("div", {"class": "wprm-recipe-time"})[0].get_text()
        )

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.findAll("li", {"class": "wprm-recipe-ingredient"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.findAll("li", {"class": "wprm-recipe-instruction"})

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
