from ._abstract import AbstractScraper
from ._utils import get_equipment


class SimpleGreenSmoothies(AbstractScraper):
    @classmethod
    def host(cls):
        return "simplegreensmoothies.com"

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

    def equipment(self):
        equipment_items = [
            text
            for equip in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
            if (text := equip.get_text())
        ]
        return get_equipment(equipment_items)
