from ._abstract import AbstractScraper
from ._utils import normalize_string


class FattoInCasaDaBenedetta(AbstractScraper):
    @classmethod
    def host(cls):
        return "fattoincasadabenedetta.it"

    def instructions(self):
        step_divs = self.soup.find_all("div", {"class": "step"})

        all_instructions = []
        for step in step_divs:
            instruction_text = normalize_string(step.get_text())
            if instruction_text:
                all_instructions.append(instruction_text)

        return "\n".join(all_instructions)

    def equipment(self):
        return list(
            dict.fromkeys(
                (item.get_text()) for item in self.soup.find_all("p", class_="name")
            )
        )
