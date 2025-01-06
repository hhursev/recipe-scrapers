from ._abstract import AbstractScraper
from ._utils import get_equipment


class GlutenFreeOnAShoeString(AbstractScraper):
    @classmethod
    def host(cls):
        return "glutenfreeonashoestring.com"

    def equipment(self):
        equipment_items = [
            equip.get_text()
            for equip in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
            if equip.get_text()
        ]
        return get_equipment(equipment_items)
