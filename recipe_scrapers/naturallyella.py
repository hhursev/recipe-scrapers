from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class NaturallyElla(AbstractScraper):
    @classmethod
    def host(cls):
        return "naturallyella.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h5",
            ".wprm-recipe-ingredient-group li",
        )
