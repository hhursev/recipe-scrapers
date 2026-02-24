from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class BakeEatRepeat(AbstractScraper):
    @classmethod
    def host(cls):
        return "bake-eat-repeat.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".mv-create-ingredients h4",
            ".mv-create-ingredients li",
        )
