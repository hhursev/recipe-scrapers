from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class AndyCooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "andy-cooks.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".rk_ingredients .rk_group_heading",
            ".rk_ingredients ul li",
        )
