from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class CleanEatingKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "cleaneatingkitchen.com"

    def ingredients(self):
        ingredients = [
            ingredient.get_text(" ", strip=True)
            for ingredient in self.soup.select(
                ".tasty-recipes-ingredients ul li:not(:has(strong))"
            )
        ]
        return ingredients

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".tasty-recipes-ingredients ul li:has(strong)",
            ".tasty-recipes-ingredients ul li:not(:has(strong))",
        )
