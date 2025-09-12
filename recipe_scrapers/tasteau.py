from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class TasteAU(AbstractScraper):
    @classmethod
    def host(cls):
        return "taste.com.au"

    def ingredients(self):
        ingredient_elements = self.soup.select("div.ingredient-description")
        ingredients = [
            element["data-raw-ingredient"] for element in ingredient_elements
        ]
        return ingredients

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "li.section-heading h3",
            "div.ingredient-description",
        )

    def instructions(self):
        instructions = self.schema.instructions()

        filtered_instructions = [
            line
            for line in instructions.split("\n")
            if not line.lower().startswith("step")
        ]

        return "\n".join(filtered_instructions)
