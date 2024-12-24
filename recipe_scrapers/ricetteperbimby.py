from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class RicettePerBimby(AbstractScraper):
    @classmethod
    def host(cls):
        return "ricetteperbimby.it"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ricetta-ingredienti .label",
            ".ricetta-ingredienti .ingrediente",
        )
