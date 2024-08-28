import re

from ._abstract import AbstractScraper
from ._exceptions import FieldNotProvidedByWebsiteException


class Chefnini(AbstractScraper):
    @classmethod
    def host(cls):
        return "chefnini.com"

    def author(self):
        return "chefNini"

    def title(self):
        return self.soup.find("span", {"itemprop": "headline"}).get_text()

    def total_time(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def yields(self):
        recipe_yields_text = self.soup.find(
            "h3", {"itemprop": "recipeYield"}
        ).get_text()
        servings = re.match(r"Pour (\d+)", recipe_yields_text).group(1)
        return f"{servings} servings"

    def ingredients(self):
        ingredients = self.soup.findAll("li", {"itemprop": "ingredients"})
        return [ingredient.get_text() for ingredient in ingredients]

    def instructions(self):
        instruction_list = [
            instruction.get_text()
            for instruction in self.soup.find(
                "div", {"itemprop": "recipeInstructions"}
            ).children
            if instruction.get_text().strip()
        ]

        return "\n".join(instruction_list)

    def ratings(self):
        return None

    def cuisine(self):
        return None

    def description(self):
        return self.soup.find("p", {"itemprop": "description"}).get_text()
