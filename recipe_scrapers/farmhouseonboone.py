from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class FarmhouseOnBoone(AbstractScraper):
    @classmethod
    def host(cls):
        return "farmhouseonboone.com"

    def equipment(self):
        return list(
            dict.fromkeys(
                (equip.find("a").get_text())
                for equip in self.soup.find_all(
                    "div", class_="wprm-recipe-equipment-name"
                )
                if equip.find("a") and equip.find("a").get_text()
            )
        )

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group .wprm-recipe-group-name",
            ".wprm-recipe-ingredient",
        )
