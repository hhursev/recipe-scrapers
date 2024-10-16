from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml, StaticValueException
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class TimesOfIndia(AbstractScraper):
    @classmethod
    def host(cls):
        return "recipes.timesofindia.com"

    def site_name(self):
        raise StaticValueException(return_value="Times of India - Recipes")

    def ingredients(self):
        container = self.soup.find("div", id="ingredata")
        if not container:
            raise ElementNotFoundInHtml("Could not find ingredient data container")

        ingredients = container.find_all("label", attrs={"class": "clearfix"})
        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def language(self):
        meta_language = self.soup.find("meta", attrs={"http-equiv": "content-language"})

        return normalize_string(meta_language.get("content"))

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".specialingrs span",
            "ul[data-convert] label.clearfix",
        )
