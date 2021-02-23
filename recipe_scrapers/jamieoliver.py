from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class JamieOliver(AbstractScraper):
    @classmethod
    def host(cls):
        return "jamieoliver.com"

    def title(self) -> Optional[str]:
        return self.soup.find("h1").get_text()

    def total_time(self) -> Optional[int]:
        return get_minutes(self.soup.find("div", {"class": "time"}))

    def yields(self) -> Optional[str]:
        return get_yields(self.soup.find("div", {"class": "recipe-detail serves"}))

    def image(self) -> Optional[str]:
        container = self.soup.find("div", {"class": "recipe-header-left"})
        if not container:
            return None

        image = container.find("img", {"src": True})
        return image["src"] if image else None

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.find("ul", {"class", "ingred-list"}).findAll("li")

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.find("div", {"class": "instructions-wrapper"})
        return normalize_string(instructions.get_text())
