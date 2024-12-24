from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_equipment


class ElaVegan(AbstractScraper):
    @classmethod
    def host(cls):
        return "elavegan.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient-group li",
        )

    def equipment(self):
        equipment_items = [
            item.find("div", class_="wprm-recipe-equipment-name")
            .get_text()
            .rstrip("*")
            .strip()
            for item in self.soup.find_all("div", class_="wprm-recipe-equipment-item")
            if item.find("div", class_="wprm-recipe-equipment-name")
        ]
        return get_equipment(equipment_items)
