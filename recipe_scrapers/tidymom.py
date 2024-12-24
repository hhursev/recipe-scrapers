from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class TidyMom(AbstractScraper):
    @classmethod
    def host(cls):
        return "tidymom.net"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".mv-create-ingredients h4",
            ".mv-create-ingredients li",
        )
