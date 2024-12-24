from ._abstract import AbstractScraper
from ._utils import normalize_string


class GesundAktiv(AbstractScraper):
    @classmethod
    def host(cls):
        return "gesund-aktiv.com"

    def author(self):
        return self.site_name()

    def ingredients(self):
        ingredients_container = self.soup.find(
            "div", {"class": "news-recipes-indgredients"}
        )
        ingredients = ingredients_container.findAll("li")
        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]
