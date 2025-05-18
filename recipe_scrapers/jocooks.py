from ._abstract import AbstractScraper
from ._utils import get_equipment


class JoCooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "jocooks.com"

    def equipment(self):
        equipment_items = [
            item.get_text()
            for item in self.soup.find_all("li", class_="wprm-recipe-equipment-item")
        ]
        return get_equipment(equipment_items)
