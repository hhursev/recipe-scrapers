from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import csv_to_tags, get_equipment


class TheKitchenMagPie(AbstractScraper):
    @classmethod
    def host(cls):
        return "thekitchenmagpie.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )

    def equipment(self):
        equipment_container = self.soup.select_one(".wprm-recipe-details-container")
        if equipment_container:
            equipment_text = equipment_container.find("dt", string="Equipment")
            if equipment_text:
                equipment_list = equipment_text.find_next_sibling(name="dd")
                if equipment_list:
                    return get_equipment(csv_to_tags(equipment_list.text))
        return None
