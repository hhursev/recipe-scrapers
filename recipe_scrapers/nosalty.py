from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class NoSalty(AbstractScraper):
    @classmethod
    def host(cls):
        return "nosalty.hu"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".p-recipe__ingredients .m-list__title",
            ".p-recipe__ingredients .m-list__item",
        )
