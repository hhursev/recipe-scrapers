# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class BlueJeanChef(AbstractScraper):
    @classmethod
    def host(cls):
        return "bluejeanchef.com"

    def category(self):
        return self.schema.category()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h5",
            ".wprm-recipe-ingredients li",
        )

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
