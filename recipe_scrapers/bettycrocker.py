# mypy: disallow_untyped_defs=False
# BettyCrocker.com scraper
# Written by G.D. Wallters
# Freely released the code to recipe_scraper group
# 18 January, 2020
# =======================================================


from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class BettyCrocker(AbstractScraper):
    @classmethod
    def host(cls):
        return "bettycrocker.com"

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
            self.soup,
            ".recipeIngredients h3",
            ".recipeIngredients li",
        )

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()
