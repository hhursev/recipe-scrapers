# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients, normalize_string


class TheSpruceEats(AbstractScraper):
    @classmethod
    def host(cls):
        return "thespruceeats.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients = self.soup.select("li.structured-ingredients__list-item p")
        extracted_ingredients = []
        for ingredient in ingredients:
            extracted_ingredients.append(normalize_string(ingredient.text))

        return extracted_ingredients

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "p.structured-ingredients__list-heading",
            "li.structured-ingredients__list-item p",
        )

    def instructions(self):
        return self.schema.instructions()
