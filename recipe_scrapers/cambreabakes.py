from ._abstract import AbstractScraper
from ._utils import get_equipment


class CambreaBakes(AbstractScraper):
    @classmethod
    def host(cls):
        return "cambreabakes.com"

    def equipment(self):
        equipment_items = self.soup.select(
            ".wprm-recipe-equipment.wprm-recipe-equipment-list .wprm-recipe-equipment-item .wprm-recipe-equipment-name"
        )
        equipment_list = [item.get_text(strip=True) for item in equipment_items]

        return get_equipment(equipment_list)
