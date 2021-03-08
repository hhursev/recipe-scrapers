from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class ClosetCooking(AbstractScraper):
    @classmethod
    def host(cls):
        return "closetcooking.com"

    def title(self):
        return normalize_string(
            self.soup.find("h1", {"class": "entry-title"}).get_text()
        )

    def total_time(self):
        return get_minutes(self.soup.find(itemprop="totalTime").parent)

    def yields(self):
        return get_yields(self.soup.find(itemprop="recipeYield").parent)

    def ingredients(self):
        ingredients = self.soup.findAll("li", {"itemprop": "recipeIngredient"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.findAll("li", {"itemprop": "recipeInstructions"})

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
