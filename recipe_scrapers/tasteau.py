# mypy: allow-untyped-defs

import re

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class TasteAU(AbstractScraper):
    @classmethod
    def host(cls):
        return "taste.com.au"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "li.section-heading h3",
            "div.ingredient-description",
        )

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        description_html = self.schema.description()
        description_text = re.sub("<[^>]*>", "", description_html)
        return description_text
