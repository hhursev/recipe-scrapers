import re
from typing import List, Optional

from ._abstract import AbstractScraper

BULLET_CHARACTER_ORD = 8226


class NutritionByNathalie(AbstractScraper):
    ingredientMatch = re.compile(r"Ingredients:")

    @classmethod
    def host(cls):
        return "nutritionbynathalie.com"

    def title(self) -> Optional[str]:
        return self.soup.find("h1").get_text()

    def total_time(self) -> Optional[int]:
        return 0

    def yields(self) -> Optional[str]:
        return None

    def image(self) -> Optional[str]:
        try:
            return self.soup.find("img", {"id": re.compile(r"^innercomp_")})["src"]
        except Exception:
            return None

    def ingredients(self) -> Optional[List[str]]:
        ingredients = []

        elements = self.soup.find_all(text=self.ingredientMatch)
        for outerElement in elements:
            title = outerElement.find_parent("p")
            if not title:
                continue
            element = title.nextSibling
            while element:
                ingredient = element.get_text()
                if len(ingredient) == 0 or ord(ingredient[0]) != BULLET_CHARACTER_ORD:
                    break
                ingredients.append(ingredient[2:])
                element = element.nextSibling

        return ingredients

    def instructions(self) -> Optional[str]:
        title = self.soup.find(text="Directions:").find_parent("p")

        instructions = []
        for child in title.nextSibling.find_all("li"):
            instructions.append(child.get_text())

        return "\n".join(instructions)

    def ratings(self) -> Optional[float]:
        return None
