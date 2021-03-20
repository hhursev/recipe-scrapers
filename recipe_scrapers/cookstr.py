from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class Cookstr(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookstr.com"

    def title(self) -> Optional[str]:
        return normalize_string(
            self.soup.find("h1", {"class": "articleHeadline"}).get_text()
        )

    def total_time(self) -> Optional[int]:
        sections = self.soup.findAll("div", {"class": "articleAttrSection"})
        total_time = 0
        for section in sections:
            time = section.find(text="Total Time")
            if time:
                total_time += get_minutes(time.parent.parent)
        return total_time

    def yields(self) -> Optional[str]:
        sections = self.soup.findAll("span", {"class": "attrLabel"})
        for section in sections:
            serves = section.find(text="Serves")
            if serves:
                return get_yields(serves.parent.parent)
        raise Exception("Servings amount not found")

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.find("div", {"class": "recipeIngredients"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients.findAll("li")
        ]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.find("div", {"class": "stepByStepInstructionsDiv"})

        return "\n".join(
            [
                normalize_string(instruction.get_text())
                for instruction in instructions.findAll("p")
            ]
        )
