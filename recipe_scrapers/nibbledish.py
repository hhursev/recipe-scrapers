# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import normalize_string


class NibbleDish(AbstractScraper):
    @classmethod
    def host(cls):
        return "nibbledish.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        schema_ingredients = self.schema.ingredients()

        # Good case: multiple ingredients were found
        if len(schema_ingredients) > 1:
            return schema_ingredients

        # Fallback case: to handle situations where all ingredient text has been merged
        # into a single recipeIngredient metadata item.
        container = self.soup.find("div", {"class": "recipe-ingredients"})
        ingredients = container.find_all("li")

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        schema_instructions = self.schema.ingredients()

        # Good case: multiple instructions were found
        if len(schema_instructions) > 1:
            return schema_instructions

        # Fallback case: to handle situations where all instruction text has been merged
        # into a single recipeInstruction metadata item.
        container = self.soup.find("div", {"class": "recipe-instructions"})
        instructions = container.find_all("li")

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def ratings(self):
        return self.schema.ratings()
