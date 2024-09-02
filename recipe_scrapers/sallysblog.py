from urllib.parse import unquote

from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._utils import get_minutes, normalize_string


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
                ).text
                title = ingredient.find(
                    "span",
                    {
                        "class": "shop-studio-recipes-recipe-detail-tabs-description-ingredients__content__ingredient-list__ingredient__title"
                    },
                ).text
                ingredients.append(f"{quantity} {title}")

        return ingredients

    def author(self):
        return "Sally's Blog"
