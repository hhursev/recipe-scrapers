from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class HassanChef(AbstractScraper):
    @classmethod
    def host(cls):
        return "hassanchef.com"

    def author(self):
        return self.schema.author().title()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            '#recipe-card p[style*="font-style: italic"]',
            '#recipe-card ul[itemprop="recipeIngredient"] li',
        )
