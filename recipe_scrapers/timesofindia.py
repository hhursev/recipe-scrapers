from ._abstract import AbstractScraper
from ._utils import normalize_string


class TimesOfIndia(AbstractScraper):
    @classmethod
    def host(cls):
        return "recipes.timesofindia.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients = self.soup.find_all("label", attrs={"class": "clearfix"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def language(self):
        meta_language = self.soup.find("meta", attrs={"http-equiv": "content-language"})

        return normalize_string(meta_language.get("content"))

    def cuisine(self):
        return self.schema.cuisine()
