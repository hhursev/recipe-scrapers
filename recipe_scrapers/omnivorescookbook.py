from ._abstract import AbstractScraper
from ._utils import normalize_string


class OmnivoresCookbook(AbstractScraper):
    @classmethod
    def host(cls):
        return "omnivorescookbook.com"

    def ingredients(self):
        ingredients = self.soup.find_all("li", {"class": "wprm-recipe-ingredient"})
        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def description(self):
        return self.soup.head.find("meta", {"property": "og:description"})["content"]
