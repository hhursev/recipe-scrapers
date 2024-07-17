from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class Arla(AbstractScraper):
    @classmethod
    def host(cls):
        return "arla.se"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "div.u-mt--m > h5",
            "div.u-mt--m > table > tbody > tr",
        )
