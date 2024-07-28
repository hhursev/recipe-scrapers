from recipe_scrapers._grouping_utils import group_ingredients

from ._abstract import AbstractScraper
from ._exceptions import StaticValueException


class Matprat(AbstractScraper):
    @classmethod
    def host(cls):
        return "matprat.no"

    def site_name(self):
        raise StaticValueException(return_value="MatPrat")

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup.find("div", "ingredients-list"),
            "h3.ingredient-section-title",
            "ul.ingredientsList > li > span:not(.amount):not(.unit)",
        )

    def nutrients(self):
        nutrient_names = [
            x.text for x in self.soup("td", "recipe-nutritions__table-cell-name")
        ]
        if not nutrient_names:
            return None
        nutrient_values = [
            x.text.replace("\xa0", " ")
            for x in self.soup("td", "recipe-nutritions__table-cell-value")
        ]
        return dict(zip(nutrient_names, nutrient_values))
