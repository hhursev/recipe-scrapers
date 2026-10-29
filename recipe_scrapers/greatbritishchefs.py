from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients, IngredientGroup
from ._utils import get_yields


class GreatBritishChefs(AbstractScraper):
    @classmethod
    def host(cls):
        return "greatbritishchefs.com"

    def ingredient_groups(self):
        groups = group_ingredients(
            self.ingredients(),
            self.soup,
            "#recipe-ingredients-start div[id] > h4",
            "#recipe-ingredients-start div[id] > ul > li",
        )

        if len(groups) == 1 and groups[0].purpose == self.title():
            return [IngredientGroup(ingredients=self.ingredients())]

        return groups

    def yields(self):
        serves = self.soup.select_one(".gbcicon-serves")
        if not serves:
            return None

        return get_yields(serves.parent.get_text())
