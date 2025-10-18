from ._abstract import AbstractScraper
from ._exceptions import FieldNotProvidedByWebsiteException


class KFoods(AbstractScraper):
    @classmethod
    def host(cls):
        return "kfoods.com"

    def language(self):
        # HTML meta lang attribute is in place, but does not reliably describe the recipe language
        raise FieldNotProvidedByWebsiteException()

    def ingredients(self):
        schema_ingredient_data = self.schema.data.get("recipeIngredient")
        if isinstance(schema_ingredient_data, list):
            if len(schema_ingredient_data) == 1:
                combined_ingredients = schema_ingredient_data[0]
                if "\n" in combined_ingredients:
                    return combined_ingredients.split("\n")
        return schema_ingredient_data

    def instructions(self):
        schema_instructions = self.schema.instructions()
        trimmed_instructions = [
            line.strip() for line in schema_instructions.split("\n")
        ]
        return "\n".join(trimmed_instructions)
