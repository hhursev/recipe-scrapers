from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class BiancaZapatka(AbstractScraper):
    @classmethod
    def host(cls):
        return "biancazapatka.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient-group li",
        )
