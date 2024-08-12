from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class AltonBrown(AbstractScraper):
    @classmethod
    def host(cls):
        return "altonbrown.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )

    def equipment(self):
        return list(
            dict.fromkeys(
                (equip.get_text())
                for equip in self.soup.find_all(
                    "div", class_="wprm-recipe-equipment-name"
                )
            )
        )
