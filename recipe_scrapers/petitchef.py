from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class PetitChef(AbstractScraper):
    @classmethod
    def host(cls):
        return "en.petitchef.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "#rd-ingredients .i-title",
            "#rd-ingredients .il",
        )
