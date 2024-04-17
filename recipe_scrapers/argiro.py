from ._abstract import AbstractScraper
from ._utils import get_equipment, normalize_string


class Argiro(AbstractScraper):
    @classmethod
    def host(cls):
        return "argiro.gr"

    def equipment(self):
        equipment_items = [
            normalize_string(e.get_text())
            for e in self.soup.find_all("div", class_="equipment-title")
        ]
        return get_equipment(equipment_items)
