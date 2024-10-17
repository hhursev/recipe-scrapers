from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_equipment


class BrokenOvenBaking(AbstractScraper):
    @classmethod
    def host(cls):
        return "brokenovenbaking.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )

    def equipment(self):
        equipment_items = self.soup.select(
            ".wprm-recipe-equipment-container .wprm-recipe-equipment-item"
        )
        equipment_list = [
            item.select_one(".wprm-recipe-equipment-name").get_text()
            for item in equipment_items
        ]

        return get_equipment(equipment_list)
