from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class TheOldWomanAndTheSea(AbstractScraper):
    @classmethod
    def host(cls):
        return "theoldwomanandthesea.com"

    def description(self):
        return self.soup.find("meta", {"property": "og:description"}).get("content")

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".tasty-recipes-ingredients-body h4",
            ".tasty-recipes-ingredients-body p",
        )
