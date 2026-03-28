from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class AllSavoryRecipes(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "allsavoryrecipes.com"

    def instructions(self):
        instructions = self.schema.instructions()
        filtered_instructions = "\n".join(
            line for line in instructions.split("\n") if not line.startswith("Step")
        )
        return filtered_instructions
