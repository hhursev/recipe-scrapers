from ._abstract import AbstractScraper
from ._utils import get_equipment, normalize_string


class Joyfoodsunshine(AbstractScraper):
    @classmethod
    def host(cls):
        return "joyfoodsunshine.com"

    def ingredients(self):
        ingredients = self.soup.findAll("li", {"class": "wprm-recipe-ingredient"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def equipment(self):
        equipment_items = [
            text
            for equip in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
            if (text := equip.get_text())
        ]
        return get_equipment(equipment_items)
