from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class HowToFeedALoon(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "howtofeedaloon.com"

    def ingredients(self):
        ingredients_list = []
        for el in self.soup.select(".wprm-recipe-ingredient"):
            amount = el.select_one(".wprm-recipe-ingredient-amount")
            unit = el.select_one(".wprm-recipe-ingredient-unit")
            name = el.select_one(".wprm-recipe-ingredient-name")
            notes = el.select_one(".wprm-recipe-ingredient-notes")

            ingredient_parts = [
                amount.get_text(strip=True) if amount else None,
                unit.get_text(strip=True) if unit else None,
                name.get_text(strip=True) if name else None,
                notes.get_text(strip=True) if notes else None,
            ]

            ingredient = " ".join(filter(None, ingredient_parts))
            ingredients_list.append(ingredient)

        return ingredients_list
