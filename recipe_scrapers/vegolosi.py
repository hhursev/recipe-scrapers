from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class Vegolosi(AbstractScraper):
    @classmethod
    def host(cls):
        return "vegolosi.it"

    def title(self):
        return self.soup.find("h1").get_text().strip()

    def preparation_time(self):
        possible_time_info_elements = self.soup.findAll(
            "span", {"class": "tasty-recipes-prep-time"}
        )

        return sum([get_minutes(element) for element in possible_time_info_elements])

    def cooking_time(self):
        possible_time_info_elements = self.soup.findAll(
            "span", {"class": "tasty-recipes-cook-time"}
        )

        return sum([get_minutes(element) for element in possible_time_info_elements])

    def total_time(self):
        possible_time_info_elements = self.soup.findAll(
            "span", {"class": "tasty-recipes-total-time"}
        )

        return sum([get_minutes(element) for element in possible_time_info_elements])

    def yields(self):
        possible_yields_info_elements = self.soup.findAll(
            "span", {"class": "tasty-recipes-yield"}
        )
        for element in possible_yields_info_elements:
            if "persone" in element.get_text():
                return get_yields(element)
        return ""

    def ingredients(self):
        ingredients = self.soup.select(".tasty-recipe-ingredients > ul > li")

        if not ingredients:
            ingredients = self.soup.findAll("li", {"class": "ingredient"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):

        instructions = self.soup.findAll("div", {"class": "tasty-recipe-instructions"})

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def ratings(self):
        return round(
            float(
                self.soup.find("div", {"class": "tasty-recipe-rating rating_panel"})
                .get("data-content-rate")
                .replace(",", ".")
            ),
            2,
        )
