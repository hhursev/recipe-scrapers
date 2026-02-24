from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class ThePioneerWoman(AbstractScraper):
    @classmethod
    def host(cls):
        return "thepioneerwoman.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredients-body h3",
            ".ingredient-lists li",
        )

    def instructions(self):
        instructions = self.schema.instructions()
        if instructions == "":
            instructions_element = self.soup.select_one(".directions")
            if instructions_element:
                instructions = instructions_element.get_text(separator="\n")
        return instructions
