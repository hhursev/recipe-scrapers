from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class HEB(AbstractScraper):
    @classmethod
    def host(self, domain="com"):
        return f"www.heb.{domain}"

    def title(self) -> Optional[str]:
        return self.soup.find("h1", {"class": "title"}).get_text()

    def total_time(self) -> Optional[int]:
        minutes_tag = self.soup.find("div", {"itemprop": "totalTime"})
        return get_minutes(minutes_tag.parent.get_text())

    def yields(self) -> Optional[str]:
        yields_tag = self.soup.find("div", {"itemprop": "recipeYield"})
        return get_yields(yields_tag.parent.get_text())

    def ingredients(self) -> Optional[List[str]]:
        ingredients_container = self.soup.find(class_="ingredientswrapper")
        ingredients = ingredients_container.findAll("div", {"class": "recipestepstxt"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self) -> Optional[str]:
        instructions_container = self.soup.find("div", {"class": "instructions"})
        instructions = instructions_container.findAll(
            "span", {"class": "instructiontxt"}
        )
        return [
            normalize_string(instruction.get_text()) for instruction in instructions
        ]

    def image(self) -> Optional[str]:
        container = self.soup.find("div", {"class": "recipeimage"})
        if not container:
            return None

        image = container.find("img", {"src": True})
        return image["src"] if image else None
