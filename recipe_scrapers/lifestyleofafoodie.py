from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class LifestyleOfAFoodie(AbstractScraper):
    @classmethod
    def host(cls):
        return "lifestyleofafoodie.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "div.wprm-recipe-ingredient-group h4",
            "ul.wprm-recipe-ingredients li",
        )

    def equipment(self):
        return list(
            dict.fromkeys(
                (item.get_text())
                for item in self.soup.find_all(
                    "div", class_="wprm-recipe-equipment-name"
                )
            )
        )
