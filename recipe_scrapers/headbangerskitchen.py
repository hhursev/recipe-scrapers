from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class HeadbangersKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "headbangerskitchen.com"

    def author(self):
        return "Sahil Makhija"

    def title(self):
        return self.soup.find("span", {"class": "wpurp-recipe-title"}).get_text()

    def total_time(self):
        prepTime = int(
            (self.soup.find("span", {"class": "wpurp-recipe-prep-time"}).get_text())
        )

        cookTime = int(
            (self.soup.find("span", {"class": "wpurp-recipe-cook-time"}).get_text())
        )

        return get_minutes(prepTime + cookTime)

    def yields(self):
        return get_yields(self.soup.find("span", {"class": "wpurp-recipe-servings"}))

    # def image(self):
    #     return self.schema.image()

    def ingredients(self):
        ingredients = self.soup.findAll(
            "ul", {"class": "wpurp-recipe-ingredient-container"}
        )

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.findAll(
            "ol", {"class": "wpurp-recipe-instruction-container"}
        )

        return [
            normalize_string(instruction.get_text()) for instruction in instructions
        ]

    # def ratings(self):
    #     return self.schema.ratings()
