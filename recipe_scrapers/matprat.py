# mypy: disallow_untyped_defs=False
from recipe_scrapers._grouping_utils import group_ingredients

from ._abstract import AbstractScraper


class Matprat(AbstractScraper):
    @classmethod
    def host(cls):
        return "matprat.no"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup.find("div", "ingredients-list"),
            "h3.ingredient-section-title",
            "ul.ingredientsList > li > span:not(.amount):not(.unit)",
        )

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def description(self):
        return self.schema.description()

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
