from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class RufflesAndRainboots(AbstractScraper):
    @classmethod
    def host(cls):
        return "rufflesandrainboots.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".mv-create-ingredient-group-header h4",
            ".mv-create-ingredient-list li",
        )
