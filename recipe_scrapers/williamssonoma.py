from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class WilliamsSonoma(AbstractScraper):
    @classmethod
    def host(cls):
        return "williams-sonoma.com"

    def author(self):
        return "Williams Sonoma"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".botLeft > h3",
            ".botLeft > ul > li",
        )
