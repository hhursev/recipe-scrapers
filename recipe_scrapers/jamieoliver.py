from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class JamieOliver(AbstractScraper):
    @classmethod
    def host(cls):
        return "jamieoliver.com"

    def instructions(self):
        method_heading = self.soup.find("h2", string="Method")
        instructions_list = method_heading.find_next(name="ol")
        instructions = instructions_list.find_all("li")
        return "\n".join([normalize_string(inst.get_text()) for inst in instructions])

    def ingredients(self):
        ingredients_list = self.soup.select(".ingredients-rich-text p.type-body")
        return [
            normalize_string(ingredient.get_text()) for ingredient in ingredients_list
        ]

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredients-rich-text p.type-h5",
            ".ingredients-rich-text p.type-body",
        )
