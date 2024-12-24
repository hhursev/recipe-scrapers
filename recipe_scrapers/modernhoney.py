from ._abstract import AbstractScraper
from ._utils import get_equipment


class ModernHoney(AbstractScraper):
    @classmethod
    def host(cls):
        return "modernhoney.com"

    def equipment(self):
        equipment_items = [
            item.get_text()
            for item in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
        ]
        return get_equipment(equipment_items)
