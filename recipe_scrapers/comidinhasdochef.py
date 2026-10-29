from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class ComidinhasDoChef(AbstractScraper):
    @classmethod
    def host(cls):
        return "comidinhasdochef.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".content-text-shadow h2.subtitle",
            ".content-text-shadow ul li",
        )

    def instructions(self):
        instructions = self.schema.instructions()

        filtered_instructions = [
            line
            for line in instructions.split("\n")
            if not line.lower().startswith("passo")
        ]

        return "\n".join(filtered_instructions)
