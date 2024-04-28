# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class McCormick(AbstractScraper):
    @classmethod
    def host(cls):
        return "mccormick.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

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

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
