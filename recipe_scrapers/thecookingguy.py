# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._utils import get_yields, normalize_string


class TheCookingGuy(AbstractScraper):
    @classmethod
    def host(cls):
        return "thecookingguy.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return get_yields(self.soup.find("div", class_="text-block-7").get_text())

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients = self.soup.find("div", class_="w-layout-vflex card-text-holder ingredients").find_all("li")
        ingredients_text = [normalize_string(ingredient.get_text()) for ingredient in ingredients]
        return ingredients_text

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        description = self.soup.find("div", class_="richintro w-richtext").find("p")
        description_text = normalize_string(description.get_text())
        return description_text
