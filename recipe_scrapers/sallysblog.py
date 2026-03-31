from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup, group_ingredients


class SallysBlog(AbstractScraper):
    @classmethod
    def host(cls):
        return "sallys-blog.de"

    def ingredients(self):
        ingredients = []
        groupings = self.soup.find_all(
            "div",
            {
                "class": "shop-studio-recipes-recipe-detail-tabs-description-ingredients__content__ingredient-list"
            },
        )
        for grouping in groupings:
            ingredient_items = grouping.find_all(
                "div",
                {
                    "class": "shop-studio-recipes-recipe-detail-tabs-description-ingredients__content__ingredient-list__ingredient"
                },
                recursive=False,
            )
            for ingredient in ingredient_items:
                quantity = ingredient.find(
                    "span",
                    {
                        "class": "shop-studio-recipes-recipe-detail-tabs-description-ingredients__content__ingredient-list__ingredient__quantity"
                    },
                )
                title = ingredient.find(
                    "span",
                    {
                        "class": "shop-studio-recipes-recipe-detail-tabs-description-ingredients__content__ingredient-list__ingredient__title"
                    },
                )
                ingredients.append(f"{quantity.text} {title.text}")

        return ingredients

    def author(self):
        return "Sally's Blog"

    def ingredient_groups(self):
        groups = group_ingredients(
            self.ingredients(),
            self.soup,
            ".shop-studio-recipes-recipe-detail-tabs-description-ingredients__content__ingredient-list__title",
            ".shop-studio-recipes-recipe-detail-tabs-description-ingredients__content__ingredient-list__ingredient",
        )

        if len(groups) > 1:
            return groups
        else:
            return [IngredientGroup(ingredients=self.ingredients(), purpose=None)]
