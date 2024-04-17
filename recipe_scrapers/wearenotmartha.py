# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class WeAreNotMartha(AbstractScraper):
    @classmethod
    def host(cls):
        return "wearenotmartha.com"

    def category(self):
        return self.schema.category()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            "ul.wprm-recipe-ingredients li",
        )

    def cuisine(self):
        return self.schema.cuisine()
