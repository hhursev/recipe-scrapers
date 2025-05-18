from ._abstract import AbstractScraper
from ._utils import get_equipment


class BudgetBytes(AbstractScraper):
    @classmethod
    def host(cls):
        return "budgetbytes.com"

    def equipment(self):
        equipment_items = [
            link.get_text()
            for link in self.soup.select(
                "div.wprm-recipe-equipment-name a.wprm-recipe-equipment-link"
            )
        ]
        return get_equipment(equipment_items)
