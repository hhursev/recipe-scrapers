from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class TudoGostoso(AbstractScraper):
    @classmethod
    def host(cls):
        return "tudogostoso.com.br"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".recipe-ingredients-subtitle",
            ".recipe-ingredients-item",
        )
