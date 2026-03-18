from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class TasteOfHome(AbstractScraper):
    @classmethod
    def host(cls):
        return "tasteofhome.com"

    def ingredients(self):
        ingredient_elements = self.soup.select(
            ".ingredient-item:not(.sub-ingredient-title)"
        )
        ingredients = []
        for ingredient in ingredient_elements:
            ingredient_text = ingredient.get_text(strip=True)
            ingredients.append(ingredient_text)
        return ingredients

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredient-item.sub-ingredient-title",
            ".ingredients-list > .ingredient-item:not(.sub-ingredient-title), .sub-ingredients .ingredient-item",
        )
