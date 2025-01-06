from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._grouping_utils import group_ingredients


class TheVintageMixer(AbstractScraper):
    @classmethod
    def host(cls):
        return "thevintagemixer.com"

    def site_name(self):
        raise StaticValueException(return_value="Vintage Mixer")

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )
