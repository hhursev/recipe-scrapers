from recipe_scrapers._grouping_utils import IngredientGroup

from ._abstract import AbstractScraper


class MyKoreanKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "mykoreankitchen.com"

    def ingredient_groups(self):
        ingredient_groups = self.soup.find_all(
            "div", {"class": "wprm-recipe-ingredient-group"}
        )

        results = []
        index_base = 0

        for ingredient_group in ingredient_groups:

            count = index_base + len(ingredient_group.find_all("li"))

            purpose_heading = ingredient_group.find(
                "h4", "wprm-recipe-ingredient-group-name"
            )
            results.append(
                IngredientGroup(
                    ingredients=self.schema.ingredients()[index_base:count],
                    purpose=purpose_heading.text if purpose_heading else None,
                )
            )

            index_base = count

        return results
