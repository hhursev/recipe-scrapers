from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class TheVintageMixer(AbstractScraper):
    @classmethod
    def host(cls):
        return "thevintagemixer.com"

    def title(self) -> Optional[str]:
        return self.soup.find("h2", {"class": "wprm-recipe-name"}).get_text()

    def total_time(self) -> Optional[int]:
        return get_minutes(
            self.soup.find("span", {"class": "wprm-recipe-total_time-minutes"}).parent
        )

    def image(self) -> Optional[str]:
        container = self.soup.find("div", {"class": "wprm-recipe-image"})
        if not container:
            return None

        image = container.find("img", {"src": True})
        return image["src"] if image else None

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.findAll("li", {"class": "wprm-recipe-ingredient"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
            if len(normalize_string(ingredient.get_text())) > 0
        ]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.findAll(
            "div", {"class": "wprm-recipe-instruction-text"}
        )

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
