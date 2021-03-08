from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class MyBakingAddiction(AbstractScraper):
    @classmethod
    def host(cls):
        return "mybakingaddiction.com"

    def title(self):
        return self.soup.find("h1").get_text()

    def total_time(self):
        return get_minutes(
            self.soup.find("div", {"class": "mv-create-time-total"}).get_text()
        )

    def yields(self):
        return get_yields(self.soup.find("div", {"class": "mv-create-time-yield"}))

    def ingredients(self):
        ingredients = self.soup.find("div", {"class": "mv-create-ingredients"}).findAll(
            "li"
        )

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.find(
            "div", {"class": "mv-create-instructions"}
        ).findAll("li")

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def ratings(self):
        rating = self.soup.find("div", {"class": "mv-create-reviews"}).attrs.get(
            "data-mv-create-rating", None
        )

        return round(float(rating), 2)
