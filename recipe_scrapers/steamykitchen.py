from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class SteamyKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "steamykitchen.com"

    def title(self):
        return self.soup.find("h2", {"itemprop": "name"}).get_text()

    def total_time(self):
        return sum(
            [
                get_minutes(self.soup.find(itemprop="prepTime").parent),
                get_minutes(self.soup.find(itemprop="cookTime").parent),
            ]
        )

    def yields(self):
        return get_yields(self.soup.find("span", itemprop="recipeYield"))

    def image(self):
        image = self.soup.find("img", {"itemprop": "image", "src": True})
        return image["src"] if image else None

    def ingredients(self):
        ingredients = self.soup.findAll("span", {"itemprop": "ingredients"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
            if len(normalize_string(ingredient.get_text())) > 0
        ]

    def instructions(self):
        instructions = self.soup.find("div", {"class": "instructions"}).findAll("p")

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
