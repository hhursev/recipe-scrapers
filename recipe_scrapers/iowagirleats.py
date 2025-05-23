from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class IowaGirlEats(AbstractScraper):
    @classmethod
    def host(cls):
        return "iowagirleats.com"

    def author(self):
        return self.soup.find("meta", {"name": "author"})["content"]

    def instructions(self):
        instructions = self.soup.find_all(
            "div", {"class": "wprm-recipe-instruction-text"}
        )
        instruction_list = []

        for instruction in instructions:
            instruction_list.append(instruction.get_text().strip())

        return "\n".join(instruction_list)

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )
