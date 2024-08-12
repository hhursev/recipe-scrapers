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
