from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class McCormick(AbstractScraper):
    @classmethod
    def host(cls):
        return "mccormick.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".recipe-about-list .substitutions-title",
            ".recipe-about-list li:not(.substitutions-title):not(.substitutions-content li)",
        )

    def instructions(self):
        instructions = self.schema.instructions()

        filtered_instructions = [
            line
            for line in instructions.split("\n")
            if not line.lower().startswith("step")
        ]

        return "\n".join(filtered_instructions)
