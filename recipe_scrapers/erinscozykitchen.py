from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class ErinsCozyKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "erinscozykitchen.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".recipe-ingredients .dr-title",
            ".recipe-ingredient",
        )
