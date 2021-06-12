from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class WhatsGabyCooking(AbstractScraper):
    @classmethod
    def host(cls):
        return "whatsgabycooking.com"

    def title(self):
        return self.soup.find("h1", {"class": "entry-title"}).get_text()

    def total_time(self):
        return get_minutes(self.soup.find("p", {"class": "header-recipe-time"}))

    def yields(self):
        return self.schema.yields()

    def ingredients(self):
        ingredients = self.soup.findAll("li", {"class": "wprm-recipe-ingredient"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
            if len(ingredient) > 0
        ]

    def instructions(self):
        instructions = self.soup.findAll("li", {"class": "wprm-recipe-instruction"})

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
