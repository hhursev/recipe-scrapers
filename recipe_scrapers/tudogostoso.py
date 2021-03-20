from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class TudoGostoso(AbstractScraper):
    @classmethod
    def host(cls):
        return "tudogostoso.com.br"

    def title(self) -> Optional[str]:
        return normalize_string(self.soup.find("h1").get_text())

    def total_time(self) -> Optional[int]:
        return get_minutes(self.soup.find("time", {"class": "dt-duration"}))

    def ingredients(self) -> Optional[List[str]]:
        ingredients_html = self.soup.findAll("span", {"class": "p-ingredient"})

        return [
            normalize_string(ingredient.get_text()) for ingredient in ingredients_html
        ]

    def instructions(self) -> Optional[str]:
        instructions_html = self.soup.findAll(
            "div", {"class": "instructions e-instructions"}
        )

        return "\n".join(
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        )
