from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class PaniniHappy(AbstractScraper):
    @classmethod
    def host(cls):
        return "paninihappy.com"

    def title(self) -> Optional[str]:
        return self.soup.find("h1", {"class": "entry-title"}).get_text()

    def total_time(self) -> Optional[int]:
        return get_minutes(self.soup.find("span", {"class": "duration"}))

    def yields(self) -> Optional[str]:
        return get_yields(self.soup.find("span", {"class": "yield"}))

    def image(self) -> Optional[str]:
        image = self.soup.find("img", {"class": "post_image", "src": True})
        return image["src"] if image else None

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.findAll("li", {"class": "ingredient"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.findAll("li", {"class": "instruction"})

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
