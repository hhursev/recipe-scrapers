from ._abstract import AbstractScraper
from ._utils import get_equipment


class SizzlingEats(AbstractScraper):
    @classmethod
    def host(cls):
        return "sizzlingeats.com"

    def instructions(self):
        instructions = self.soup.find_all(
            "div", {"class": "wprm-recipe-instruction-text"}
        )
        return "\n".join([instruction.get_text() for instruction in instructions])

    def equipment(self):
        equipment_items = [
            text
            for equip in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
            if (text := equip.get_text())
        ]
        return get_equipment(equipment_items)
