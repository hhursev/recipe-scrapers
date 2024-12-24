from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_equipment, normalize_string


class AmazingRibs(AbstractScraper):
    @classmethod
    def host(cls):
        return "amazingribs.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredients li",
        )

    def equipment(self):
        equipment_items = [
            normalize_string(e.get_text())
            for e in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
        ]
        return sorted(get_equipment(equipment_items))
