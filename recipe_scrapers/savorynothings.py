from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_equipment


class SavoryNothings(AbstractScraper):
    @classmethod
    def host(cls):
        return "savorynothings.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )

    def equipment(self):
        equipment_items = [
            link.get_text()
            for link in self.soup.select(
                "div.wprm-recipe-equipment-name a.wprm-recipe-equipment-link"
            )
        ]
        equipment_items += [
            item.get_text()
            for item in self.soup.select(
                "div.wprm-recipe-equipment-name:not(:has(a.wprm-recipe-equipment-link))"
            )
        ]
        return get_equipment(equipment_items)
