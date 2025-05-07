from ._abstract import AbstractScraper
from ._utils import get_equipment


class HungryHappens(AbstractScraper):
    @classmethod
    def host(cls):
        return "hungryhappens.net"

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
