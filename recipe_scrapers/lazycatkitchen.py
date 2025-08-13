from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class LazyCatKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "lazycatkitchen.com"

    def ingredient_groups(self):
        groups = group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredients-section p",
            ".ingredients-section li",
        )
        if len(groups) == 1 and (
            not groups[0].purpose or groups[0].purpose.strip().lower() == "ingredients"
        ):
            return [type(groups[0])(ingredients=groups[0].ingredients, purpose=None)]
        return groups
