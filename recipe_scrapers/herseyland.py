# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._utils import get_equipment


class HerseyLand(AbstractScraper):
    @classmethod
    def host(cls):
        return "hersheyland.com"

    def author(self):
        return "Herseyland"

    def category(self):
        return self.schema.category()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

    def equipment(self):
        equipment_items = [
            item.find("span", class_="h6").get_text()
            for item in self.soup.find_all("div", class_="equipment-item")
            if item.find("span", class_="h6")
        ]
        return get_equipment(equipment_items)
