# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


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
        soup = self.soup
        ingredients = soup.findAll("li", {"class": "structured-ingredients__list-item"})

        extracted_ingredients = []
        for ingredient in ingredients:
            quantity_span = ingredient.find(
                "span", {"data-ingredient-quantity": "true"}
            )
            unit_span = ingredient.find("span", {"data-ingredient-unit": "true"})
            name_span = ingredient.find("span", {"data-ingredient-name": "true"})

            if quantity_span and unit_span and name_span:
                extracted_ingredients.append(
                    f"{normalize_string(quantity_span.text)} "
                    f"{normalize_string(unit_span.text)} "
                    f"{normalize_string(name_span.text)}"
                )

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
