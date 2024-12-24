from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_equipment


class BakingSense(AbstractScraper):
    @classmethod
    def host(cls):
        return "baking-sense.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient-group li",
        )

    def equipment(self):
        equipment_items = [
            equip.get_text()
            for equip in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
            if equip.get_text()
        ]
        return get_equipment(equipment_items)
