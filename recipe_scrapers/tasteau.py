# mypy: allow-untyped-defs

import re

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class TasteAU(AbstractScraper):
    @classmethod
    def host(cls):
        return "taste.com.au"

    def category(self):
        return self.schema.category()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "li.section-heading h3",
            "div.ingredient-description",
        )

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        description_html = self.schema.description()
        description_text = re.sub("<[^>]*>", "", description_html)
        return description_text
