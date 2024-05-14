# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
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
