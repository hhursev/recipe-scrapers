from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class Saveur(AbstractScraper):
    @classmethod
    def host(cls):
        return "saveur.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.soup.find("h1").get_text()

    def total_time(self):
        prep_time = self.soup.find("meta", {"property": "prepTime"})
        cook_time = self.soup.find("meta", {"property": "cookTime"})
        return sum(
            [
                get_minutes(prep_time.get("content")) if prep_time else 0,
                get_minutes(cook_time.get("content")) if cook_time else 0,
            ]
        )

    def yields(self):
        return get_yields(
            self.soup.find("span", {"property": "recipeYield"}).get_text()
        )

    def ingredients(self):
        ingredients = self.soup.findAll("li", {"property": "recipeIngredient"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.findAll("li", {"property": "recipeInstructions"})

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
