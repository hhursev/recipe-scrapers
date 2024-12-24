from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_equipment


class PeelWithZeal(AbstractScraper):
    @classmethod
    def host(cls):
        return "peelwithzeal.com"

    def equipment(self):
        equipment_items = [
            equip.get_text()
            for equip in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
            if equip.get_text()
        ]
        return get_equipment(equipment_items)

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )
