from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class AmericasTestKitchen(AbstractScraper):

    @classmethod
    def host(cls):
        return "americastestkitchen.com"

    def ingredients(self):
        return [
            ingredient.replace(" ,", ",") for ingredient in self.schema.ingredients()
        ]

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "h3.mise-text",
            'span[class^="recipePrintBody_ingredient__"]',
        )
