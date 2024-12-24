from ._abstract import AbstractScraper
from ._utils import get_equipment, normalize_string


class OneSweetAppetite(AbstractScraper):
    @classmethod
    def host(cls):
        return "onesweetappetite.com"

    def equipment(self):
        equipment_items = [
            normalize_string(e.get_text())
            for e in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
        ]
        return get_equipment(equipment_items)
