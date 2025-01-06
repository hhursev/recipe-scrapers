from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class WellPlated(AbstractScraper):
    @classmethod
    def host(cls):
        return "wellplated.com"

    def cuisine(self):
        return self.schema.cuisine().replace(",", ", ")

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-group-name",
            ".wprm-recipe-ingredient",
        )
