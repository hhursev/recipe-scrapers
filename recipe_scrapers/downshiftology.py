from ._abstract import AbstractScraper
from ._utils import get_equipment


class Downshiftology(AbstractScraper):
    @classmethod
    def host(cls):
        return "downshiftology.com"

    def equipment(self):
        equipment_items = [
            item.find("a", class_="wprm-recipe-equipment-link").get_text()
            for item in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
            if item.find("a", class_="wprm-recipe-equipment-link")
        ]
        return get_equipment(equipment_items)
