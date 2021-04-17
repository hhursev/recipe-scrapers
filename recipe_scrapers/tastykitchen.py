from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class TastyKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "tastykitchen.com"

    def title(self):
        return self.soup.find("h1", {"itemprop": "name"}).get_text()

    def total_time(self):
        return sum(
            [
                get_minutes(self.soup.find("time", {"itemprop": "prepTime"})),
                get_minutes(self.soup.find("time", {"itemprop": "cookTime"})),
            ]
        )

    def yields(self):
        return get_yields(self.soup.find("span", {"itemprop": "yield"}))

    def image(self):
        image = self.soup.find("img", {"class": "the_recipe_image", "src": True})
        return image["src"] if image else None

    def ingredients(self):
        ingredients = self.soup.find("ul", {"class": "ingredients"}).findAll("li")

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.find("span", {"itemprop": "instructions"}).findAll("p")

        return "\n".join(
            [normalize_string(direction.get_text()) for direction in instructions]
        )
