from ._abstract import AbstractScraper
from ._utils import get_equipment


class BrokenOvenBaking(AbstractScraper):
    @classmethod
    def host(cls):
        return "brokenovenbaking.com"

    def equipment(self):
        equipment_items = [
            text
            for equip in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
            if (text := equip.get_text())
        ]
        return get_equipment(equipment_items)
