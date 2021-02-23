from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class SimplyRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "simplyrecipes.com"

    def title(self) -> Optional[str]:
        return self.soup.find("h1").get_text()

    def total_time(self) -> Optional[int]:
        return get_minutes(
            self.soup.find("div", {"class": "total-time"})
            .find("span", {"class": "meta-text__data"})
            .text
        )

    def yields(self) -> Optional[str]:
        return get_yields(
            normalize_string(
                self.soup.find("div", {"class": "recipe-serving"})
                .find("span", {"class": "meta-text__data"})
                .text
            )
        )

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.find("ul", {"class": "ingredient-list"}).findAll("li")

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self) -> Optional[str]:
        steps = self.soup.find(
            "div", {"class": "structured-project__steps"}
        ).ol.findAll("li")

        return "\n".join(
            [
                normalize_string(
                    step.h3.text + ": " + "".join([p.text for p in step.findAll("p")])
                )
                for step in steps
            ]
        )
