from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class SallysBakingAddiction(AbstractScraper):
    @classmethod
    def host(cls):
        return "sallysbakingaddiction.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".tasty-recipes-ingredients-body h4",
            "li[data-tr-ingredient-checkbox]",
        )
