from ._abstract import AbstractScraper
import re


class SamsungFood(AbstractScraper):
    @classmethod
    def host(cls):
        return "app.samsungfood.com"

    def ingredients(self):
        schema_ingredients = self.schema.ingredients()
        return [ingredient.lstrip("- ").strip() for ingredient in schema_ingredients]

    def instructions(self):
        schema_instructions = self.schema.instructions()
        cleaned_instructions = [
            re.sub(r"^\d+\.\s*", "", line).strip()
            for line in schema_instructions.split("\n")
        ]
        return "\n".join(cleaned_instructions)

    def nutrients(self):
        schema_nutrients = self.schema.nutrients()

        if not schema_nutrients or not isinstance(schema_nutrients, dict):
            raise ValueError("Unexpected or missing nutrients data from schema.")

        parsed_nutrients = {}
        for nutrient, value in schema_nutrients.items():
            if "calories" in nutrient.lower():
                match = re.search(r"\d+(\.\d+)?", str(value))
                if match:
                    parsed_nutrients["calories"] = match.group(0)
            else:
                parsed_nutrients[nutrient] = str(value).strip('"')

        return parsed_nutrients
