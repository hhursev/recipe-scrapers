from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class FamilyfoodOnTheTable(AbstractScraper):
    @classmethod
    def host(cls):
        return "familyfoodonthetable.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "h3",
            ".mv-create-ingredients li",
        )
