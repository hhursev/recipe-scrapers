from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class CookieAndKate(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookieandkate.com"

    def title(self):
        return self.soup.find("h1", {"class": "entry-title"}).get_text()

    def total_time(self):
        return get_minutes(
            self.soup.find("span", {"class": "tasty-recipes-total-time"})
        )

    def yields(self):
        yields = self.soup.find("span", {"class": "tasty-recipes-yield"}).get_text()

        return get_yields("{} servings".format(yields))

    def ingredients(self):
        ingredients = self.soup.find(
            "div", {"class": "tasty-recipe-ingredients"}
        ).find_all("li")

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.find(
            "div", {"class": "tasty-recipe-instructions"}
        ).find_all("li")

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def ratings(self):
        return round(float(self.soup.find("span", {"class": "average"}).get_text()), 2)
