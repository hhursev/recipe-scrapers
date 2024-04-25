# mypy: allow-untyped-defs

from recipe_scrapers._exceptions import ElementNotFoundInHtml
from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers._utils import get_minutes

from ._abstract import AbstractScraper


class MyKoreanKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "mykoreankitchen.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def ingredient_groups(self) -> list[IngredientGroup]:
        ingredient_list = self.soup.find_all(
            "div", {"class": "wprm-recipe-ingredient-group"}
        )

        ingredient_groups = []
        ingredient_index_base = 0

        for ingredient_group in ingredient_list:

            ingredient_count = (
                len(ingredient_group.find_all("li")) + ingredient_index_base
            )

            ingredient_groups.append(
                IngredientGroup(
                    [
                        ingredient
                        for ingredient in self.schema.ingredients()[
                            ingredient_index_base:ingredient_count
                        ]
                    ],
                    (
                        ingredient_group.find(
                            "h4", "wprm-recipe-ingredient-group-name"
                        ).text
                        if ingredient_group.find(
                            "h4", "wprm-recipe-ingredient-group-name"
                        )
                        is not None
                        else "MAIN"
                    ),
                )
            )

            ingredient_index_base = ingredient_count

        return ingredient_groups

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

    def cook_time(self):
        recipe_time = self.soup.find(
            "div", {"class": "wprm-recipe-prep-time-container"}
        )
        try:
            return get_minutes(recipe_time)
        except ElementNotFoundInHtml:
            return None

    def prep_time(self):
        recipe_time = self.soup.find(
            "div", {"class": "wprm-recipe-cook-time-container"}
        )
        try:
            return get_minutes(recipe_time)
        except ElementNotFoundInHtml:
            return None
