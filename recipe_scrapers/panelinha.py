import re

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string

INSTRUCTIONS_NUMBERING_REGEX = re.compile(r"^\d{1,2}\.\s*")  # noqa


class Panelinha(AbstractScraper):
    @classmethod
    def host(cls):
        return "panelinha.com.br"

    def ingredients(self):
        ingredients = self.soup.find("h5", string="Ingredientes").nextSibling.findAll(
            "li"
        )

        return [
            normalize_string(ingredient.get_text().replace("\u00C2", ""))
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = self.soup.find(
            "h5", string="Modo de preparo"
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
        main_element = self.soup.find("main")
        yield_text = main_element.get("data-item-p-yield")
        yield_number = re.search(r"\d+", yield_text)
        if yield_number:
            return get_yields(yield_number.group())

    def total_time(self):
        tempo_de_preparo = (
            self.soup.find("dt", string="Tempo de preparo").find_next("dd").text
        )
        return get_minutes(tempo_de_preparo)
