from ._abstract import AbstractScraper
from ._utils import normalize_string


class AHealthySliceOfLife(AbstractScraper):
    @classmethod
    def host(cls):
        return "ahealthysliceoflife.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients = self.soup.find(
            "div", {"class": "tasty-recipes-ingredients-body"}
        ).find_all("p")
        return [normalize_string(ing.get_text().strip()) for ing in ingredients]

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
