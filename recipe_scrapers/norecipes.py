from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class NoRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "norecipes.com"

    def _cleaned_ingredients(self):
        ingredients_list = self.schema.ingredients()
        return [
            ingredient.replace("((", "(").replace("))", ")")
            for ingredient in ingredients_list
        ]

    def ingredients(self):
        return self._cleaned_ingredients()

    def ingredient_groups(self):
        cleaned_ingredients = self._cleaned_ingredients()
        return group_ingredients(
            cleaned_ingredients,
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient-group li",
        )
