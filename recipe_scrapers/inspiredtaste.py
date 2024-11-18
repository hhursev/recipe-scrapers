from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class InspiredTaste(AbstractScraper):
    @classmethod
    def host(cls):
        return "inspiredtaste.net"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredient_heading",
            ".itr-ingredients p",
        )
