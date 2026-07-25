from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class RicardoCuisine(AbstractScraper):
    @classmethod
    def host(cls):
        return "ricardocuisine.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".c-recipe-instructions--ingredients .c-recipe-instructions__subtitle",
            ".c-recipe-instructions--ingredients .c-recipe-instructions__item",
        )
