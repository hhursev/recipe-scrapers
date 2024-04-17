# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_equipment


class BudgetBytes(AbstractScraper):
    @classmethod
    def host(cls):
        return "budgetbytes.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )

    def ratings(self):
        return self.schema.ratings()

    def equipment(self):
        equipment_items = [
            link.get_text()
            for link in self.soup.select(
                "div.wprm-recipe-equipment-name a.wprm-recipe-equipment-link"
            )
        ]
        return get_equipment(equipment_items)
