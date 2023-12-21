# mypy: allow-untyped-defs

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
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".h5.padding-bottom-5.padding-top-5",
            "ul > li[itemprop='recipeIngredient']",
        )

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def language(self):
        return self.soup.find("meta", {"property": "og:locale"}).get("content")

    def site_name(self):
        return "Mundo de Receitas Bimby"
