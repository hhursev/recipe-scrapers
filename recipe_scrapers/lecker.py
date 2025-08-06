from ._abstract import AbstractScraper
from ._utils import normalize_string


class Lecker(AbstractScraper):
    @classmethod
    def host(cls):
        return "lecker.de"

    def instructions(self):
        instruction_steps = self.soup.select(
            ".bx-instruction-group__instruction-step + div p"
        )
        normalized_instructions = [
            normalize_string(step.get_text()) for step in instruction_steps
        ]
        return "\n".join(normalized_instructions)
