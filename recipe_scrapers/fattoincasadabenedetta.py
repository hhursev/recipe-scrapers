# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._utils import normalize_string


class FattoInCasaDaBenedetta(AbstractScraper):
    @classmethod
    def host(cls):
        return "fattoincasadabenedetta.it"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        step_divs = self.soup.find_all("div", {"class": "step"})

        all_instructions = []
        for step in step_divs:
            instruction_text = normalize_string(step.get_text())
            if instruction_text:
                all_instructions.append(instruction_text)

        return "\n".join(all_instructions)

    def ratings(self):
        return self.schema.ratings()

    def description(self):
        return self.schema.description()

    def equipment(self):
        return list(
            dict.fromkeys(
                (item.get_text()) for item in self.soup.find_all("p", class_="name")
            )
        )
