from ._abstract import AbstractScraper
from ._utils import get_equipment


class Thinlicious(AbstractScraper):
    @classmethod
    def host(cls):
        return "thinlicious.com"

    def equipment(self):
        equipment_list = self.soup.select(".wprm-recipe-equipment-name")
        return get_equipment(item.get_text() for item in equipment_list)
