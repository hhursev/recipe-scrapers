from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class Yamasa(AbstractScraper):
    @classmethod
    def host(cls):
        return "recipe.yamasa.com"

    def ingredients(self):
        return [
            " ".join(i.stripped_strings)
            for i in self.soup.select(".ingredients .ingredient")
        ]

    def instructions(self):
        instructions = self.schema.instructions()

        filtered_instructions = [
            line
            for line in instructions.split("\n")
            if line.strip().lower() != "preparation"
        ]

        return "\n".join(filtered_instructions)

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".group-head",
            ".ingredient",
        )
