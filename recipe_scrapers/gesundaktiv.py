from ._abstract import AbstractScraper
from ._utils import normalize_string


class GesundAktiv(AbstractScraper):
    @classmethod
    def host(cls):
        return "gesund-aktiv.com"

    def ingredients(self):
        ingredients_container = self.soup.find(
            "div", {"class": "news-recipes-indgredients"}
        )
        ingredients = ingredients_container.findAll("li")
        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def author(self):
        author_tag = self.soup.find("meta", {"property": "og:site_name"})
        if author_tag:
            return normalize_string(author_tag.get("content"))
        return None
