from ._abstract import AbstractScraper
from ._utils import get_equipment


class CulinaryHill(AbstractScraper):
    @classmethod
    def host(cls):
        return "culinaryhill.com"

    def ingredients(self):
        return [
            li.get_text(" ", strip=True).replace("▢", "").strip()
            for li in self.soup.select(
                "ul.wprm-recipe-ingredients > li.wprm-recipe-ingredient"
            )
        ]

    def equipment(self):
        equipment_items = [
            text
            for equip in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
            if (text := equip.get_text())
        ]
        return get_equipment(equipment_items)
