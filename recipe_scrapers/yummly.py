from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class Yummly(AbstractScraper):
    @classmethod
    def host(cls):
        return "yummly.com"

    def title(self) -> Optional[str]:
        return self.soup.find("h1").get_text()

    def total_time(self) -> Optional[int]:
        return get_minutes(self.soup.find("div", {"class": "recipe-summary-item unit"}))

    def yields(self) -> Optional[str]:
        return get_yields(
            self.soup.find("div", {"class": "servings"}).find("input").get("value")
        )

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.findAll("li", {"class": "IngredientLine"})

        return [
            " ".join(
                [
                    normalize_string(span.get_text())
                    for span in ingredient.select(
                        """
                    span[class^=amount],
                    span[class^=unit],
                    span[class^=ingredient]"""
                    )
                ]
            )
            for ingredient in ingredients
        ]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.find("div", attrs={"class": "directions-wrapper"})
        return (
            "\n".join(
                [
                    normalize_string(instr.get_text())
                    for instr in instructions.findAll("span", attrs={"class": "step"})
                ]
            )
            if instructions is not None
            else None
        )
