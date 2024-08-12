from ._abstract import AbstractScraper
from ._utils import normalize_string


class JustOneCookbook(AbstractScraper):
    @classmethod
    def host(cls):
        return "justonecookbook.com"

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
