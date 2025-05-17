from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class Culy(AbstractScraper):
    @classmethod
    def host(cls):
        return "culy.nl"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredients h3",
            ".ingredients ul li[itemprop='ingredients'], .ingredients ul li",
        )

    def instructions(self):
        instructions_list = self.soup.select("ol li")
        cleaned_instructions = [
            instruction.get_text(strip=True) for instruction in instructions_list
        ]
        return "\n".join(cleaned_instructions)
