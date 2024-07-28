from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class AllTomat(AbstractScraper):
    @classmethod
    def host(cls):
        return "alltommat.se"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredients-section h2",
            ".ingredients-list li",
        )
