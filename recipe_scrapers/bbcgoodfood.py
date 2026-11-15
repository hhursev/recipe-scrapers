from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class BBCGoodFood(AbstractScraper):
    @classmethod
    def host(cls):
        return "bbcgoodfood.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "h3.ingredients-list__heading",
            "li.ingredients-list__item",
        )
