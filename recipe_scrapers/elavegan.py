from ._abstract import AbstractScraper
from ._utils import get_equipment


class ElaVegan(AbstractScraper):
    @classmethod
    def host(cls):
        return "elavegan.com"

    def equipment(self):
        equipment_items = [
            item.find("div", class_="wprm-recipe-equipment-name")
            .get_text()
            .rstrip("*")
            .strip()
            for item in self.soup.find_all("div", class_="wprm-recipe-equipment-item")
            if item.find("div", class_="wprm-recipe-equipment-name")
        ]
        return get_equipment(equipment_items)
