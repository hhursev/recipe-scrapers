# mypy: allow_untyped_defs

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class AmazingRibs(AbstractScraper):
    @classmethod
    def host(cls):
        return "amazingribs.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ingredients(self):
        return self.schema.ingredients()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredients li",
        )

    def instructions(self):
        return self.schema.instructions()

    def equipment(self):
        equipment_list = self.soup.find_all("div", class_="wprm-recipe-equipment-name")
        if not equipment_list:
            return []

        unique_equipment = {
            normalize_string(equipment.get_text()) for equipment in equipment_list
        }
        return list(unique_equipment)
