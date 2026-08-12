from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class JournalDesFemmes(AbstractScraper):
    @classmethod
    def host(cls):
        return "cuisine.journaldesfemmes.fr"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".app_recipe_ing_category",
            ".app_recipe_ing_item",
        )
