from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class MundoDeReceitasBimby(AbstractScraper):
    @classmethod
    def host(cls):
        return "mundodereceitasbimby.com.pt"

    def author(self):
        return normalize_string(
            self.soup.find("span", class_="recipe-author").find("a").text
        )

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".h5.padding-bottom-5.padding-top-5",
            "ul > li[itemprop='recipeIngredient']",
        )

    def language(self):
        return self.soup.find("meta", {"property": "og:locale"}).get("content")

    def site_name(self):
        return "Mundo de Receitas Bimby"
