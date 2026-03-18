from ._abstract import AbstractScraper
from ._wprm import WPRMMixin
from ._utils import normalize_string


class Joyfoodsunshine(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "joyfoodsunshine.com"

    def ingredients(self):
        ingredients = self.soup.find_all("li", {"class": "wprm-recipe-ingredient"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]
