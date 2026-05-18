from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class GoodFoodDiscoveries(AbstractScraper):
    @classmethod
    def host(cls):
        return "goodfooddiscoveries.com"

    def ingredients(self):
        # removing "u003cbu003e" and "u003c/bu003e" as it looks to be used at times to bold text on the site
        return [
            ingredient.replace("u003cbu003e", "").replace("u003c/bu003e", "")
            for ingredient in self.schema.ingredients()
        ]

    def description(self):
        return self.soup.find("p", {"class": "recipe-card-summary"}).get_text()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredient-item-group-title",
            ".ingredient-item:not(.ingredient-item-group)",
        )
