from ._abstract import AbstractScraper
from ._wprm import WPRMMixin
from ._grouping_utils import group_ingredients


class LifestyleOfAFoodie(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "lifestyleofafoodie.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "div.wprm-recipe-ingredient-group h4",
            "ul.wprm-recipe-ingredients li",
        )
