from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class ThePioneerWoman(AbstractScraper):
    @classmethod
    def host(cls):
        return "thepioneerwoman.com"

    def title(self):
        return self.soup.find("h3", {"class": "recipe-title"}).get_text()

    def total_time(self):
        return sum(
            [
                get_minutes(dd)
                for dd in self.soup.find(
                    "div", {"class": "recipe-summary-time"}
                ).findAll("dd")
            ]
        )

    def yields(self):
        return get_yields(self.soup.find("span", {"itemprop": "recipeYield"}))

    def ingredients(self):
        ingredients = self.soup.find("ul", {"class": "list-ingredients"}).findAll("li")

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.findAll("div", {"class": "panel-body"})[-1]

        return normalize_string(instructions.get_text()).replace(".", ".\n")
