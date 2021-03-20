from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class TheHappyFoodie(AbstractScraper):
    @classmethod
    def host(cls):
        return "thehappyfoodie.co.uk"

    def title(self) -> Optional[str]:
        return self.soup.find("h1", {"class": "main-title"}).get_text()

    def total_time(self) -> Optional[int]:
        return get_minutes(
            self.soup.find("div", {"class": "recipe__data__total-time"})
        ) or sum(
            [
                get_minutes(
                    self.soup.find("div", {"class": "recipe__data__prep-time"})
                ),
                get_minutes(
                    self.soup.find("div", {"class": "recipe__data__cook-time"})
                ),
            ]
        )

    def yields(self) -> Optional[str]:
        return get_yields(
            self.soup.find("div", {"class": "recipe__data__yield"}).get_text()
        )

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.find(
            "table", {"class": "recipe__ingredients-table"}
        ).findAll("tr")

        ingredients = [
            (
                ingredient.find(
                    "td", {"class": "recipe__ingredients__amount"}
                ).get_text(),
                ingredient.find(
                    "td", {"class": "recipe__ingredients__name"}
                ).get_text(),
            )
            for ingredient in ingredients
        ]

        return [
            normalize_string("{} {}".format(amount, name))
            for amount, name in ingredients
        ]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.find("div", {"class": "recipe__instructions"}).findAll(
            "p"
        )

        return "\n".join(
            normalize_string(instruction.get_text()) for instruction in instructions
        )
