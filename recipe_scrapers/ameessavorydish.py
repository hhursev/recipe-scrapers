from ._abstract import AbstractScraper
from ._wprm import WPRMMixin
from ._grouping_utils import group_ingredients


class AmeesSavoryDish(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "ameessavorydish.com"

    def ingredients(self):
        ingredients_list = []
        for element in self.soup.select(".wprm-recipe-ingredient:not(:has(strong))"):
            ingredient_text = " ".join(
                span.get_text(strip=True)
                for span in element.select(
                    ".wprm-recipe-ingredient-amount, "
                    ".wprm-recipe-ingredient-unit, "
                    ".wprm-recipe-ingredient-name, "
                    ".wprm-recipe-ingredient-notes"
                )
            )
            ingredients_list.append(ingredient_text)
        return ingredients_list

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group .wprm-recipe-ingredient-name strong",
            ".wprm-recipe-ingredient:not(:has(strong))",
        )
