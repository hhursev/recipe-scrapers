# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._utils import normalize_string


class JustOneCookbook(AbstractScraper):
    @classmethod
    def host(cls):
        return "justonecookbook.com"

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
        lis = self.soup.find_all("li", {"class": "wprm-recipe-ingredient"})
        ingredients = []
        for ingredient in lis:
            spans = ingredient.findAll(
                "span", class_=lambda x: x != "wprm-checkbox-container"
            )[1:]
            ingredient = []
            for span in spans:
                ingredient.append(normalize_string(span.get_text()))
            ingredients.append(" ".join(ingredient))
        return ingredients

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
