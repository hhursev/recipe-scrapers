from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class TheKitchn(AbstractScraper):
    @classmethod
    def host(cls):
        return "thekitchn.com"

    def title(self) -> Optional[str]:
        return self.soup.find("h2", {"class": "Recipe__title"}).get_text()

    def total_time(self) -> Optional[int]:
        elements = self.soup.findAll("p", {"class": "Recipe__timeEntry"})
        return sum([get_minutes(element) for element in elements])

    def yields(self) -> Optional[str]:
        return get_yields(
            self.soup.find("p", {"class": "jsx-1778438071 Recipe__yield"})
        )

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.findAll("li", {"class": "Recipe__ingredient"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.findAll("li", {"class": "Recipe__instructionStep"})

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
