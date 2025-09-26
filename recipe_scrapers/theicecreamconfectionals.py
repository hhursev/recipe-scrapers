from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class TheIceCreamConfectionals(AbstractScraper):
    @classmethod
    def host(cls):
        return "theicecreamconfectionals.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".recipe-ingredients h3.dr-title",
            ".recipe-ingredient",
        )
