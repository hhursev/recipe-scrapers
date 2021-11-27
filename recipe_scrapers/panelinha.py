import re

from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string

INSTRUCTIONS_NUMBERING_REGEX = re.compile(r"^\d{1,2}\.\s*")  # noqa


class Panelinha(AbstractScraper):
    @classmethod
    def host(cls):
        return "panelinha.com.br"

    def title(self):
        return normalize_string(self.soup.find("h1").get_text())

    def total_time(self):
        return get_minutes(
            self.soup.find("span", string="Tempo de preparo").nextSibling
        )

    def ingredients(self):
        ingredients = self.soup.find("h4", string="Ingredientes").nextSibling.findAll(
            "li"
        )

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.find(
            "h4", string="Modo de preparo"
        ).nextSibling.findAll("li")

        instructions = [
            normalize_string(instruction.get_text()) for instruction in instructions
        ]

        # Some recipes pages have a different html structure.
        if not instructions:
            instructions = self.soup.find(
                "h4", string="Modo de preparo"
            ).nextSibling.p.strings

            instructions = (
                normalize_string(instruction) for instruction in instructions
            )

            instructions = map(
                lambda step: INSTRUCTIONS_NUMBERING_REGEX.sub("", step), instructions
            )

        return "\n".join(instructions)

    def yields(self):
        return normalize_string(
            self.soup.find("span", string="Serve").nextSibling.get_text()
        )
