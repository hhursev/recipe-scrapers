# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class NutritionFacts(AbstractScraper):
    @classmethod
    def host(cls):
        return "nutritionfacts.org"

    def category(self):
        return self.schema.category()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )
