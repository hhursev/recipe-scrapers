from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class FoodRepublic(AbstractScraper):
    @classmethod
    def host(cls):
        return "foodrepublic.com"

    def title(self):
        return self.soup.find("h3", {"class": "recipe-title"}).get_text()

    def total_time(self):
        return sum(
            [
                get_minutes(self.soup.find("li", {"class": "prep-time"})),
                get_minutes(self.soup.find("li", {"class": "cook-time"})),
            ]
        )

    def yields(self):
        return get_yields(self.soup.find("span", {"itemprop": "recipeYield"}))

    def ingredients(self):
        ingredients = self.soup.findAll("li", {"itemprop": "recipeIngredient"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.find("div", {"class": "directions"}).findAll("li")

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
