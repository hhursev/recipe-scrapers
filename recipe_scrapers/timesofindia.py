from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._utils import normalize_string


class TimesOfIndia(AbstractScraper):
    @classmethod
    def host(cls):
        return "recipes.timesofindia.com"

    def site_name(self):
        raise StaticValueException(return_value="Times of India - Recipes")

    def ingredients(self):
        ingredients = self.soup.find_all("label", attrs={"class": "clearfix"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def language(self):
        meta_language = self.soup.find("meta", attrs={"http-equiv": "content-language"})

        return normalize_string(meta_language.get("content"))
