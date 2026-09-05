from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class JustAPinch(AbstractScraper):
    @classmethod
    def host(cls):
        return "justapinch.com"

    def ingredients(self):
        ingredients = []

        for item in self.soup.select(
            "#recipe-ingredients-list > li:has([data-ingredient-name])"
        ):
            quantity = item.select_one("[data-ingrient-quantity]")
            name = item.select_one("[data-ingredient-name]")

            quantity_text = quantity.get_text(" ", strip=True) if quantity else ""
            name_text = name.get_text(" ", strip=True) if name else ""

            ingredient = normalize_string(
                " ".join(filter(None, [quantity_text, name_text]))
            )
            ingredients.append(ingredient)

        return ingredients

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "#recipe-ingredients-list > li.lead",
            "#recipe-ingredients-list > li:has([data-ingredient-name])",
        )
