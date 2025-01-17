from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_equipment


class KitchenDivas(AbstractScraper):
    @classmethod
    def host(cls):
        return "kitchendivas.com"

    def equipment(self):
        equipment_container = self.soup.find(
            "div", class_="wprm-recipe-equipment-container"
        )
        if not equipment_container:
            return None
        equipment_items = [
            item.get_text(strip=True)
            for item in equipment_container.find_all(
                "div", class_="wprm-recipe-equipment-name"
            )
        ]
        return get_equipment(equipment_items)

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )
