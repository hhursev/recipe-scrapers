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
        ingredient_index_base = 0

        for ingredient_group in ingredient_groups:

            ingredient_count = (
                len(ingredient_group.find_all("li")) + ingredient_index_base
            )

            purpose_heading = ingredient_group.find(
                "h4", "wprm-recipe-ingredient-group-name"
            )
            results.append(
                IngredientGroup(
                    ingredients=[
                        ingredient
                        for ingredient in self.schema.ingredients()[
                            ingredient_index_base:ingredient_count
                        ]
                    ],
                    purpose=purpose_heading.text if purpose_heading else None,
                )
            )

            ingredient_index_base = ingredient_count

        return results
