# mypy: disallow_untyped_defs=False
import json

import requests

from ._abstract import HEADERS, AbstractScraper
from ._grouping_utils import IngredientGroup
from ._utils import _get_url_slug


class MadeWithLau(AbstractScraper):
    def __init__(self, url, proxies=None, timeout=None, *args, **kwargs):
        super().__init__(url=url, *args, **kwargs)

        recipe_slug = _get_url_slug(url)
        response = requests.get(
            "https://www.madewithlau.com/api/trpc/recipe.bySlug",
            params={"input": json.dumps({"json": {"slug": recipe_slug}})},
            headers=HEADERS,
            proxies=proxies,
            timeout=timeout,
        )

        response_json = response.json()
        self.data = response_json.get("result").get("data").get("json")

    @classmethod
    def host(cls):
        return "madewithlau.com"

    def author(self):
        return "Made With Lau"

    def title(self):
        return self.data.get("title")

    def description(self):
        return self.data.get("seoDescription")

    def prep_time(self):
        return self.data.get("prepTime")

    def total_time(self):
        return self.data.get("totalTime")

    def yields(self):
        servings = self.data.get("servings")
        return f"{servings} servings"

    def image(self):
        return self.data.get("mainImage").get("asset").get("url")

    def ingredients(self):
        ingredients = []

        for ingredient in self.data.get("ingredientsArray"):
            ingredient_type = ingredient.get("_type")
            if ingredient_type == "ingredient":
                ingredients.append(self._get_ingredient_string(ingredient))

        return ingredients

    def ingredient_groups(self):
        ingredient_groups = []

        current_purpose = None
        current_ingredients = []
        for ingredient in self.data.get("ingredientsArray"):
            ingredient_type = ingredient.get("_type")
            if ingredient_type == "ingredientSection":
                if current_ingredients or current_purpose:
                    ingredient_group = IngredientGroup(
                        ingredients=current_ingredients, purpose=current_purpose
                    )
                    ingredient_groups.append(ingredient_group)

                current_purpose = ingredient.get("section")
                current_ingredients = []
            elif ingredient_type == "ingredient":
                current_ingredients.append(self._get_ingredient_string(ingredient))

        if current_ingredients or current_purpose:
            ingredient_group = IngredientGroup(
                ingredients=current_ingredients, purpose=current_purpose
            )
            ingredient_groups.append(ingredient_group)

        return ingredient_groups

    def instructions(self):
        instructions = []
        for instruction in self.data.get("instructionsArray"):
            for part in instruction.get("freeformDescription"):
                description = ""
                for child in part.get("children"):
                    print(child.get("text"))
                    description += child.get("text")
                instructions.append(description)
        print("\n".join(instructions))
        return "\n".join(instructions)

    def category(self):
        return self.data.get("recipeCategory")

    def _get_ingredient_string(self, ingredient):
        amount = ingredient.get("amount")
        unit = ingredient.get("unit")
        item = ingredient.get("item")

        return f"{amount} {unit} {item}"
