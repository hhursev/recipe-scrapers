from __future__ import annotations

from recipe_scrapers._exceptions import ElementNotFoundInHtml
from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers._utils import get_minutes

from ._abstract import AbstractScraper


class JoyTheBaker(AbstractScraper):
    @classmethod
    def host(cls):
        return "joythebaker.com"

    def total_time(self):
        recipe_time = self.soup.find("span", {"class": "tasty-recipes-total-time"})
        try:
            return get_minutes(recipe_time)
        except ElementNotFoundInHtml:
            return None

    def ingredient_groups(self) -> list[IngredientGroup]:
        ingredients = self.soup.find("div", {"class": "tasty-recipes-ingredients-body"})

        group_titles = ingredients.find_all("p")
        ingredient_groupings = ingredients.find_all("ul")

        ingredient_groups = []

        for group_title, ingredient_group in zip(group_titles, ingredient_groupings):
            ingredient_groups.append(
                IngredientGroup(
                    [ingredient.text for ingredient in ingredient_group.find_all("li")],
                    group_title.text,
                )
            )
        return ingredient_groups

    def cook_time(self):
        recipe_time = self.soup.find("span", {"class": "tasty-recipes-cook-time"})
        try:
            return get_minutes(recipe_time)
        except ElementNotFoundInHtml:
            return None

    def prep_time(self):
        recipe_time = self.soup.find("span", {"class": "tasty-recipes-prep-time"})
        try:
            return get_minutes(recipe_time)
        except ElementNotFoundInHtml:
            return None
