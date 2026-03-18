from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class MoscatoMom(AbstractScraper):
    @classmethod
    def host(cls):
        return "moscatomom.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".mv-create-ingredients h4",
            ".mv-create-ingredients li",
        )
