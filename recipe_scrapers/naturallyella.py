from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._exceptions import FieldNotProvidedByWebsiteException


class NaturallyElla(AbstractScraper):
    @classmethod
    def host(cls):
        return "naturallyella.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h5",
            ".wprm-recipe-ingredient-group li",
        )

    def total_time(self):
        total_time = self.schema.total_time()
        if total_time:
            return total_time
        return FieldNotProvidedByWebsiteException
