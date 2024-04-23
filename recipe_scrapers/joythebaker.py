# mypy: allow-untyped-defs

from __future__ import annotations

from recipe_scrapers._grouping_utils import IngredientGroup

from ._abstract import AbstractScraper


class JoyTheBaker(AbstractScraper):
    @classmethod
    def host(cls):
        return "joythebaker.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        recipe_time = self.soup.find("span", {"class": "tasty-recipes-total-time"})
        return self._decode_time(recipe_time)

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def ingredient_groups(self) -> list[IngredientGroup]:
        ingredients = self.soup.find("div", {"class": "tasty-recipes-ingredients-body"})

        categories = ingredients.find_all("p")
        ingredient_groupings = ingredients.find_all("ul")

        ingredient_groups = []

        for index, group in enumerate(categories):
            ingredient_list = ingredient_groupings[index].find_all("li")
            ingredient_groups.append(
                IngredientGroup(
                    [ingredient.text for ingredient in ingredient_list], group.text
                )
            )

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
        recipe_time = self.soup.find("span", {"class": "tasty-recipes-cook-time"})
        return self._decode_time(recipe_time)

    def prep_time(self):
        recipe_time = self.soup.find("span", {"class": "tasty-recipes-prep-time"})
        return self._decode_time(recipe_time)

    def _decode_time(self, recipe_time) -> int | None:
        """
        Decode a time value from a given handle
        """
        if recipe_time is None:
            return None
        recipe_time_array = recipe_time.text.lower().split()
        time = 0
        for index, word in enumerate(recipe_time_array):
            try:
                int(word)
                if (
                    recipe_time_array[index + 1] == "hours"
                    or recipe_time_array[index + 1] == "hour"
                ):
                    time += int(word) * 60
                elif (
                    recipe_time_array[index + 1] == "days"
                    or recipe_time_array[index + 1] == "day"
                ):
                    time += int(word) * 1440
                else:
                    time += int(word)
            except ValueError:
                pass
        return time
