from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class ArchanasKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "archanaskitchen.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredientssubtitle",
            "li[itemprop='ingredients']",
        )
