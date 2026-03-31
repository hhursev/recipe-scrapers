from ._abstract import AbstractScraper
from ._utils import re


class Moulinex(AbstractScraper):
    @classmethod
    def host(cls):
        return "moulinex.fr"

    def ingredients(self):
        ingredients = self.schema.ingredients()
        spaced_ingredients = [
            re.sub(
                r"([0-9])([^ .0-9])", r"\1 \2", ingredient
            )  # Insert space if number is not followed by a space, period, or another number
            for ingredient in ingredients
        ]

        return spaced_ingredients

    def site_name(self):
        return "Moulinex"
