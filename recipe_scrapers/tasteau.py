from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class TasteAU(AbstractScraper):
    @classmethod
    def host(cls):
        return "taste.com.au"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "li.section-heading h3",
            "div.ingredient-description",
        )

    def description(self):
        description_text = normalize_string(self.schema.description())
        return description_text
