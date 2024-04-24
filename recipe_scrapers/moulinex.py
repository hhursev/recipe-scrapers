# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._utils import re


class Moulinex(AbstractScraper):
    @classmethod
    def host(cls):
        return "moulinex.fr"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients = self.schema.ingredients()
        spaced_ingredients = [
            re.sub(
                r"([0-9])([^ .0-9])", r"\1 \2", ingredient
            )  # Insert space if number is not followed by a space, period, or another number
            for ingredient in ingredients
        ]

        return spaced_ingredients

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def site_name(self):
        return "Moulinex"
