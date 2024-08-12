from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_equipment, normalize_string


class Unsophisticook(AbstractScraper):
    @classmethod
    def host(cls):
        return "unsophisticook.com"

    def equipment(self):
        equipment_items = [
            normalize_string(item.get_text())
            for item in self.soup.find_all(
                "div", class_="mv-create-products-product-name"
            )
        ]
        return get_equipment(equipment_items)

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".mv-create-ingredients h4",
            ".mv-create-ingredients li",
        )
