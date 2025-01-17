from ._abstract import AbstractScraper
from ._utils import get_equipment


class RecettePlus(AbstractScraper):
    @classmethod
    def host(cls):
        return "recette.plus"

    def equipment(self):
        equipment_container = self.soup.find("ul", class_="ustensiles-list")
        if not equipment_container:
            return None

        equipment_items = []
        for item in equipment_container.find_all("li", class_="ustensiles-item"):
            equipment_info = item.find("span", class_="ustensiles-info")
            if equipment_info:
                equipment_text = equipment_info.get_text().replace("  ", " ")
                equipment_items.append(equipment_text)

        return get_equipment(equipment_items)
