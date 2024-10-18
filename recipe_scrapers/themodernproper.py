from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class TheModernProper(AbstractScraper):
    @classmethod
    def host(cls):
        return "themodernproper.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".recipe-ingredients__list-title",
            ".recipe-ingredients__item",
        )
