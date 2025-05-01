from ._abstract import AbstractScraper
from ._utils import get_equipment


class BrokenOvenBaking(AbstractScraper):
    @classmethod
    def host(cls):
        return "brokenovenbaking.com"

    def equipment(self):
        equipment_items = self.soup.select(
            ".wprm-recipe-equipment-container .wprm-recipe-equipment-item"
        )
        equipment_list = [
            item.select_one(".wprm-recipe-equipment-name").get_text()
            for item in equipment_items
        ]

        return get_equipment(equipment_list)
