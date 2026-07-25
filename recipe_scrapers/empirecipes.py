from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class Empirecipes(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "empirecipes.com"

    def instructions(self):
        instructions = self.schema.instructions()
        filtered_instructions = "\n".join(
            line for line in instructions.split("\n") if not line.startswith("Step")
        )
        return filtered_instructions
