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
        equipment_items = self.soup.select(".tasty-recipes-equipment .tasty-link-card a.tasty-link")
        equipment_list = []

        for item in equipment_items:
            equipment_name = item.find_next('p').get_text(strip=True)

            if "affiliate link" not in equipment_name.lower():
                equipment_list.append(equipment_name)

        return get_equipment(equipment_list)
