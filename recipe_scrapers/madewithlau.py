import json
import math

import requests

from ._abstract import HEADERS, AbstractScraper
from ._grouping_utils import IngredientGroup
from ._utils import get_url_slug


class MadeWithLau(AbstractScraper):
    def __init__(self, url, proxies=None, timeout=None, *args, **kwargs):
        super().__init__(url=url, *args, **kwargs)

        recipe_slug = get_url_slug(url)
        response = requests.get(
            "https://www.madewithlau.com/api/trpc/recipe.bySlug",
            params={"input": json.dumps({"json": {"slug": recipe_slug}})},
            headers=HEADERS,
            proxies=proxies,
            timeout=timeout,
        )

        response_json = response.json()
        self.data = response_json.get("result").get("data").get("json")

        self.mark_defs = self._extract_mark_defs()
        self.ingredient_purposes = self._extract_ingredients_by_purpose()

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
                description = self._get_children_string(part.get("children"))
                instructions.append(self._sanitize_instruction(description))
        return "\n".join(instructions)

    def category(self):
        return self.data.get("recipeCategory")

    def _get_ingredient_string(self, ingredient):
        amount = ingredient.get("amount")
        unit = ingredient.get("unit")
        item = ingredient.get("item")

        text = f"{amount} {unit} {item}"

        notes = ingredient.get("notes", [])
        note_strings = []
        for note in notes:
            note_strings.append(self._get_children_string(note.get("children")))

        if note_strings:
            notes_string = ", ".join(note_strings)
            text += f" ({notes_string})"

        return text

    def _extract_ingredients_by_purpose(self):
        ingredient_purposes = {}

        for ingredient in self.data.get("ingredientsArray"):
            ingredient_type = ingredient.get("_type")
            if ingredient_type == "ingredient":
                purpose = ingredient.get("purpose")
                item = ingredient.get("item")
                if purpose not in ingredient_purposes:
                    ingredient_purposes[purpose] = {}

                ingredient_purposes[purpose][item] = ingredient

        return ingredient_purposes

    def _extract_mark_defs(self):
        mark_defs = {}

        for instruction in self.data.get("instructionsArray"):
            for description_part in instruction.get("freeformDescription"):
                for mark_def in description_part.get("markDefs"):
                    mark_def_key = mark_def.get("_key")
                    mark_defs[mark_def_key] = mark_def

        return mark_defs

    def _sanitize_instruction(self, instruction):
        # Removes trailing space as well as replacing all whitespace with a single space
        return " ".join(instruction.split())

    def _get_children_string(self, children):
        text = ""
        for child in children:
            child_text = child.get("text", "")

            mark_strings = []
            for mark_key in child.get("marks", []):
                mark_string = self._get_mark_string(mark_key)
                if mark_string:
                    mark_strings.append(mark_string)

            if mark_strings:
                mark_string = ", ".join(mark_strings)
                child_text += f" ({mark_string})"

            text += child_text
        return text

    def _get_ingredient(self, purpose, item):
        return self.ingredient_purposes.get(purpose, {}).get(item)

    def _get_mark_string(self, mark_key):
        mark_def = self.mark_defs.get(mark_key)
        if not mark_def:
            return None

        mark_type = mark_def.get("_type")
        if mark_type == "linkedIngredient":
            ingredient_purpose = mark_def.get("ingredientPurpose")
            ingredient_item = mark_def.get("ingredientName")

            ingredient = self._get_ingredient(ingredient_purpose, ingredient_item)

            ingredient_unit = ingredient.get("unit")
            ingredient_amount = ingredient.get("amount")
            fraction_to_use = mark_def.get("fractionToUseNow", 1)

            used_amount = self._round_and_format(ingredient_amount * fraction_to_use)

            return f"{used_amount} {ingredient_unit}"
        else:
            return None

    def _round_and_format(self, number):
        """
        Rounds to two decimal places, rounding up. If the number is a whole number, removes the trailing zeroes.
        """
        rounded_number = math.ceil(number * 100) / 100
        integer_part = int(rounded_number)
        if rounded_number == integer_part:
            return str(integer_part)
        else:
            return f"{rounded_number:.2f}"
