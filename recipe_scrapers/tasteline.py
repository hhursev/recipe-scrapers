from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class Tasteline(AbstractScraper):
    @classmethod
    def host(cls):
        return "tasteline.com"

    def ingredients(self):
        return [
            normalize_string(element.get_text(" ", strip=True))
            for element in self.soup.select("li.Ingredient")
        ]

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "h3.u-col-span-2",
            "li.Ingredient",
        )
