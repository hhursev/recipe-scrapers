from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_equipment


class JoCooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "jocooks.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )

    def equipment(self):
        equipment_items = [
            item.get_text()
            for item in self.soup.find_all("li", class_="wprm-recipe-equipment-item")
        ]
        return get_equipment(equipment_items)
