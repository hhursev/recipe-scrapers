from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_equipment


class LifestyleOfAFoodie(AbstractScraper):
    @classmethod
    def host(cls):
        return "lifestyleofafoodie.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "div.wprm-recipe-ingredient-group h4",
            "ul.wprm-recipe-ingredients li",
        )

    def equipment(self):
        equipment_items = [
            text
            for equip in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
            if (text := equip.get_text())
        ]
        return get_equipment(equipment_items)
