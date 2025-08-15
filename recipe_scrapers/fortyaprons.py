from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_equipment


class FortyAprons(AbstractScraper):
    @classmethod
    def host(cls):
        return "40aprons.com"

    def equipment(self):
        equipment_items = [
            text
            for equip in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
            if (text := equip.get_text())
        ]
        return get_equipment(equipment_items)

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "h4.wprm-recipe-group-name",
            "li.wprm-recipe-ingredient",
        )
