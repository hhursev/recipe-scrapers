# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._utils import normalize_string


class OmnivoresCookbook(AbstractScraper):
    @classmethod
    def host(cls):
        return "omnivorescookbook.com"

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
        ingredients = self.soup.find_all("li", {"class": "wprm-recipe-ingredient"})
        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.soup.head.find("meta", {"property": "og:description"})["content"]
