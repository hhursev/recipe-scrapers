# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._utils import re


class Moulinex(AbstractScraper):
    @classmethod
    def host(cls):
        return "moulinex.fr"

    def author(self):
        return self.schema.data.get("author", {}).get("name", "No author")

    def title(self):
        return self.schema.title()

    def total_time(self):
        total_time = self.schema.data["totalTime"]
        numbers = re.findall(r"\d+", total_time)

        return int(numbers[0])

    def yields(self):
        return str(self.schema.data["recipeYield"]) + " servings"

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients = self.schema.data["recipeIngredient"]
        spaced_ingredients = [
            re.sub(r"(\d)([a-zA-Z])", r"\1 \2", ingredient)
            for ingredient in ingredients
        ]

        return spaced_ingredients

    def instructions(self):
        return "\n".join(
            step["text"] for step in self.schema.data["recipeInstructions"]
        )

    def ratings(self):
        return self.schema.data.get("aggregateRating", {}).get(
            "ratingValue", "No rating"
        )

    def site_name(self):
        return "Moulinex"
