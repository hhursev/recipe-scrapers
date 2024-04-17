# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class PickUpLimes(AbstractScraper):
    @classmethod
    def host(cls):
        return "pickuplimes.com"

    def category(self):
        return self.schema.category()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(), self.soup, "h3.pt-3", ".ingredient-container"
        )

    def instructions(self):
        instructions = [
            normalize_string(e.get_text())
            for e in self.soup.find_all(class_="direction")
        ]
        return "\n".join(instructions) if instructions else None

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

    def prep_time(self):
        return self.schema.prep_time()

    def cook_time(self):
        return self.schema.cook_time()
