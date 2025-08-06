from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class ACoupleCooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "acouplecooks.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".tasty-recipes-ingredients-body p b",
            ".tasty-recipes-ingredients-body ul li",
        )

    def ingredients(self):
        ingredients_list = self.soup.select(".tasty-recipes-ingredients-body ul li")
        return [element.get_text() for element in ingredients_list]
