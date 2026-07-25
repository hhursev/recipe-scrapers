from ._abstract import AbstractScraper
from ._utils import normalize_string
from ._exceptions import FieldNotProvidedByWebsiteException
import re
import json
from typing import Optional


class Picnic(AbstractScraper):
    def __init__(self, html: str, url: str, best_image: Optional[bool] = None):
        super().__init__(html, url, best_image=best_image)
        self.recipe_data = None
        self._recipe = None
        script_tag = self.soup.find(
            "script", string=re.compile(r'\{\\"recipe\\":\{\\"id\\"')
        )

        if script_tag is None or script_tag.string is None:
            return
        recipe_regex = r'({\\"recipe\\":{.*locale.*?})'
        if html_recipe_data := re.search(recipe_regex, script_tag.string):
            recipe_match = html_recipe_data.group(1)
            recipe_parseable = recipe_match.encode("utf-8").decode("unicode_escape")
            # Fix for encoding issues
            fixed_recipe = recipe_parseable.encode("latin1").decode("utf-8")
            self.recipe_data = json.loads(fixed_recipe)
            self._recipe = self.recipe_data.get("recipe")

    @classmethod
    def host(cls):
        return "picnic.app"

    def instructions(self):
        new_instructions = []

        if self._recipe is None:
            return None

        for instruction in self._recipe["preparationInstructions"]:
            new_instructions.append(instruction["body"])
        return "\n".join(
            normalize_string(instruction) for instruction in new_instructions
        )

    def ingredients(self):
        new_ingredients = []

        if self._recipe is None:
            return None

        for ingredient in self._recipe["ingredients"]:
            qty = ingredient["displayIngredientQuantity"]
            unit = ingredient["displayUnitOfMeasurement"]
            name = ingredient["name"]
            qty = f"{qty} " if qty is not None else ""
            unit = f"{unit} " if unit is not None else ""
            new_ingredients.append(f"{qty}{unit}{name}")
        return [normalize_string(ingredient) for ingredient in new_ingredients]

    def author(self):
        return "Picnic"

    def site_name(self):
        return "Picnic"

    def title(self):
        if self._recipe:
            return self._recipe.get("name")
        return None

    def description(self):
        if self._recipe:
            return self._recipe.get("description")
        return None

    def total_time(self):
        if self._recipe:
            return self._recipe.get("preparationTimeInMinutes")
        return None

    def prep_time(self):
        if self._recipe:
            return self._recipe.get("activePreparationTimeInMinutes")
        return None

    def yields(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def language(self):
        if recipe_data := self.recipe_data:
            return recipe_data["locale"]
        return None
