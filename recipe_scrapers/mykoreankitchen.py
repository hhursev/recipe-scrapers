# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup

from ._abstract import AbstractScraper


class MyKoreanKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "mykoreankitchen.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

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

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

    def cook_time(self):
        return self.schema.cook_time()

    def prep_time(self):
        return self.schema.prep_time()
