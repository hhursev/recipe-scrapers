# mypy: allow-untyped-defs

import re

from ._abstract import AbstractScraper
from ._decorators import opengraph_fallback, schemaorg_fallback

BULLET_CHARACTER_ORD = 8226


class NutritionByNathalie(AbstractScraper):
    ingredientMatch = re.compile(r"Ingredients:")

    @classmethod
    def host(cls):
        return "nutritionbynathalie.com"

    def title(self):
        return self.soup.find("h1").get_text()

    @schemaorg_fallback
    def author(self):
        pass

    def total_time(self):
        return 0

    def yields(self):
        return None

    @opengraph_fallback
    def image(self):
        try:
            return self.soup.find("img", {"id": re.compile(r"^innercomp_")})["src"]
        except Exception:
            return None

    def ingredients(self):
        ingredients = []

        elements = self.soup.find_all(string=self.ingredientMatch)
        for outerElement in elements:
            title = outerElement.find_parent("p")
            if not title:
                continue
            for element in title.next_siblings:
                ingredient = element.get_text()
                if len(ingredient) == 0 or ord(ingredient[0]) != BULLET_CHARACTER_ORD:
                    break
                ingredients.append(ingredient[2:])
                element = element.nextSibling

        return ingredients

    def instructions(self):
        title = self.soup.find(string="Directions:").find_parent("p")

        instructions = []
        for child in title.nextSibling.find_all("li"):
            instructions.append(child.get_text())

        return "\n".join(instructions)

    def ratings(self):
        return None
