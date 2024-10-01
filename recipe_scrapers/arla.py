from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class Arla(AbstractScraper):
    @classmethod
    def host(cls):
        return "arla.se"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".c-recipe__ingredients-group h5",
            ".c-recipe__ingredients-group tr",
        )
