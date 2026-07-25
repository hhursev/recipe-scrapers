from ._abstract import AbstractScraper
from ._wprm import WPRMMixin
from ._grouping_utils import group_ingredients


class ADozenSundays(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "adozensundays.com"

    def ingredient_groups(self):
        groups = group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )
        if len(groups) == 1:
            groups[0].purpose = None
        return groups
