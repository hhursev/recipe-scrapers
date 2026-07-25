from ._abstract import AbstractScraper
from ._utils import get_yields
from ._grouping_utils import group_ingredients


class FoodRepublic(AbstractScraper):
    @classmethod
    def host(cls):
        return "foodrepublic.com"

    def yields(self):
        servings_div = self.soup.find("div", {"class": "recipe-card-servings"})
        servings_amount = (
            servings_div.find("div", {"class": "recipe-card-amount"}).text
            if servings_div
            else "0"
        )
        return get_yields(servings_amount)

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".recipe-ingredients .ingredient-section",
            ".recipe-ingredients li:not(.ingredient-section)",
        )
