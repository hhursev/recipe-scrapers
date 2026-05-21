from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class HilahCooking(AbstractScraper):
    @classmethod
    def host(cls):
        return "hilahcooking.com"

    def description(self):
        return self.soup.find("meta", {"itemprop": "description"}).get("content")

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".tasty-recipes-ingredients-body p",
            ".tasty-recipes-ingredients-body ul li",
        )
