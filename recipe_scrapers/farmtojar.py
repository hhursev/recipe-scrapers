from ._abstract import AbstractScraper
from ._utils import get_equipment


class FarmToJar(AbstractScraper):
    @classmethod
    def host(cls):
        return "farmtojar.com"

    def author(self):
        return self.soup.select_one('meta[name="author"]')["content"]

    def equipment(self):
        equipment_items = [
            text
            for equip in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
            if (text := equip.get_text())
        ]
        return get_equipment(equipment_items)
