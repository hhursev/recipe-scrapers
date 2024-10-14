from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_equipment


class HungryHappens(AbstractScraper):
    @classmethod
    def host(cls):
        return "hungryhappens.net"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )

    def equipment(self):
        equipment_container = self.soup.select_one(".wprm-recipe-equipment-container")
        if not equipment_container:
            return None

        equipment_items = [
            item.select_one(".wprm-recipe-equipment-name").get_text(strip=True)
            for item in equipment_container.select(".wprm-recipe-equipment-item")
            if item.select_one(".wprm-recipe-equipment-name")
        ]
        return get_equipment(equipment_items)
