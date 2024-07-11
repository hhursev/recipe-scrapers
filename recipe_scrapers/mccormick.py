from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


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
        instructions_list = self.soup.findAll(
            "li", {"id": lambda x: x and x.startswith("step")}
        )

        return "\n".join(
            [
                normalize_string(instruction.find("span", {"class": "para"}).get_text())
                for instruction in instructions_list
            ]
        )
