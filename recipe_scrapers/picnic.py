from ._abstract import AbstractScraper
from ._utils import normalize_string
import re
import json


class Picnic(AbstractScraper):
    def __init__(self, html: str, url: str):
        super().__init__(html, url)
        self.recipe_data = None
        script_tag = self.soup.find(
            "script", string=re.compile(r'\{\\"recipe\\":\{\\"id\\"')
        )

        if script_tag is None:
            return
        recipe_regex = r'({\\"recipe\\":{.*locale.*?})'
        if html_recipe_data := re.search(recipe_regex, script_tag.string):
            recipe_match = html_recipe_data.group(1)
            recipe_parseable = recipe_match.encode("utf-8").decode("unicode_escape")
            # Fix for encoding issues
            fixed_recipe = recipe_parseable.encode("latin1").decode("utf-8")
            self.recipe_data = json.loads(fixed_recipe)

    @classmethod
    def host(cls):
        return "picnic.app"

    def instructions(self):
        new_instructions = []

        recipe_data = self.recipe_data["recipe"]
        if recipe_data is None:
            return None

        for instruction in recipe_data["preparationInstructions"]:
            new_instructions.append(instruction["body"])
        return "\n".join(
            normalize_string(instruction) for instruction in new_instructions
        )

    def ingredients(self):
        new_ingredients = []

        recipe_data = self.recipe_data["recipe"]
        if recipe_data is None:
            return None

        for ingredient in recipe_data["ingredients"]:
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
        if recipe_data := self.recipe_data["recipe"]:
            return recipe_data["name"]
        return None

    def description(self):
        if recipe_data := self.recipe_data["recipe"]:
            return recipe_data["description"]
        return None

    def total_time(self):
        if recipe_data := self.recipe_data["recipe"]:
            return recipe_data["preparationTimeInMinutes"]
        return None

    def prep_time(self):
        if recipe_data := self.recipe_data["recipe"]:
            return recipe_data["activePreparationTimeInMinutes"]
        return None

    def yields(self):
        # not specified on the website, app seems to default to four servings with the same ingredients
        return "4 servings"

    def language(self):
        if recipe_data := self.recipe_data:
            return recipe_data["locale"]
        return None
