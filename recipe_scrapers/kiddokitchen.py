from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients, IngredientGroup


class KiddoKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "kiddokitchen.se"

    def ingredient_groups(self):
        headings = [
            h
            for h in self.soup.select("h3.text-2xl.font-semibold.mb-2")
            if h.find_next("ul")
        ]
        if len(headings) < 2:
            return [IngredientGroup(ingredients=self.ingredients())]
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "h3.text-2xl.font-semibold.mb-2",
            "ul li",
        )
