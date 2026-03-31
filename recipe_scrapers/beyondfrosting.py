from ._abstract import AbstractScraper
from ._utils import get_equipment


class BeyondFrosting(AbstractScraper):
    @classmethod
    def host(cls):
        return "beyondfrosting.com"

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
