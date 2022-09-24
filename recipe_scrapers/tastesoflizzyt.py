# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class TastesOfLizzyT(AbstractScraper):
    @classmethod
    def host(cls):
        return "tastesoflizzyt.com"

    def title(self):
        return self.soup.find("h2", {"class": "wprm-recipe-name"}).get_text()

    def total_time(self):
        return get_minutes(
            self.soup.find("div", {"class": "wprm-recipe-total-time-container"})
        )

    def yields(self):
        return get_yields(self.soup.find("span", {"class": "wprm-recipe-servings"}))

    def ingredients(self):
        ingredients = self.soup.find(
            "ul", {"class": "wprm-recipe-ingredients"}
        ).findAll("li")

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.find(
            "ul", {"class": "wprm-recipe-instructions"}
        ).findAll("li")

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
