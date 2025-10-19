from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class RealMomNutrition(AbstractScraper):
    @classmethod
    def host(cls):
        return "realmomnutrition.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".mv-create-ingredients h4",
            ".mv-create-ingredients ul li",
        )
