from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class LeitesCulinaria(AbstractScraper):
    @classmethod
    def host(cls):
        return "leitesculinaria.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-group-name",
            ".wprm-recipe-ingredient",
        )
