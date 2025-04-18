import re
from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class BakeWithZoha(AbstractScraper):
    @classmethod
    def host(cls):
        return "bakewithzoha.com"

    def ingredients(self):
        return [
            normalize_string(
                re.sub(r"\(\s*(.*?)\s*\)", r"(\1)", li.get_text(" ", strip=True))
            )
            for li in self.soup.select(".tasty-recipes-ingredients li")
        ]

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".tasty-recipes-ingredients p strong",
            ".tasty-recipes-ingredients li",
        )
