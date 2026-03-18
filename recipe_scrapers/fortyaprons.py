from ._abstract import AbstractScraper
from ._wprm import WPRMMixin
from ._grouping_utils import group_ingredients


class FortyAprons(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "40aprons.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "h4.wprm-recipe-group-name",
            "li.wprm-recipe-ingredient",
        )
