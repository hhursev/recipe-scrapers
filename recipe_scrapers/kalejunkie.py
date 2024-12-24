from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class KaleJunkie(AbstractScraper):
    @classmethod
    def host(cls):
        return "kalejunkie.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )

    def instructions(self):
        instructions = self.soup.findAll(
            "div", {"class": "wprm-recipe-instruction-text"}
        )

        return "\n".join([instruction.get_text() for instruction in instructions])
