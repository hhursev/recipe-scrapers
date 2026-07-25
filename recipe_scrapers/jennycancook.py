from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class JennyCanCook(AbstractScraper):
    @classmethod
    def host(cls):
        return "jennycancook.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "#zlrecipe-ingredients-list .ingredient-label",
            "#zlrecipe-ingredients-list .ingredient",
        )
