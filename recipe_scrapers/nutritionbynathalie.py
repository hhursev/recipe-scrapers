import re

from ._abstract import AbstractScraper
from ._utils import normalize_string

BULLET_CHARACTER_ORD = 8226


class NutritionByNathalie(AbstractScraper):
    @classmethod
    def host(cls):
        return "nutritionbynathalie.com"

    def title(self):
        return self.soup.find("h1").get_text()

    def image(self):
        try:
            return self.soup.find("img", {"id": re.compile(r"^innercomp_")})["src"]
        except Exception:
            return None

    def ingredients(self):
        ingredients = []
        element = self.soup.find(string=re.compile(r"Ingredients:"))
        parent_div = element.find_parent("div")
        paragraphs = parent_div.find_all("p")
        for paragraph in paragraphs:
            ingredient = paragraph.get_text()
            if ord(ingredient[0]) == BULLET_CHARACTER_ORD:
                ingredients.append(ingredient[2:])

        return ingredients

    def instructions(self):
        element = self.soup.find(string=re.compile("Directions:"))
        parent_div = element.find_parent("div")
        li_items = parent_div.find_all("li")

        return "\n".join([normalize_string(li_item.get_text()) for li_item in li_items])

    def ratings(self):
        return None
