from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_equipment


class BeyondFrosting(AbstractScraper):
    @classmethod
    def host(cls):
        return "beyondfrosting.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".tasty-recipes-ingredients-body p strong",
            ".tasty-recipes-ingredients-body ul li",
        )

    def equipment(self):
        equipment_items = self.soup.select(
            ".tasty-recipes-equipment .tasty-link-card a.tasty-link"
        )
        equipment_list = [
            item.find_next(name="p").get_text(strip=True)
            for item in equipment_items
            if "affiliate link"
            not in item.find_next(name="p").get_text(strip=True).lower()
        ]
        return get_equipment(equipment_list)
