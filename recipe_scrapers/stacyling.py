from ._abstract import AbstractScraper
from ._utils import get_equipment


class StacyLing(AbstractScraper):
    @classmethod
    def host(cls):
        return "stacyling.com"

    def equipment(self):
        equipment_container = self.soup.find(
            "div", class_="wprm-recipe-equipment-container"
        )
        if not equipment_container:
            return None
        equipment_items = [
            item.get_text()
            for item in equipment_container.find_all(
                "div", class_="wprm-recipe-equipment-name"
            )
        ]
        return get_equipment(equipment_items)
