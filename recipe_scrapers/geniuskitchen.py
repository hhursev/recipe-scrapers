from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class GeniusKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "geniuskitchen.com"

    def title(self):
        return (
            self.soup.find("title").get_text().replace(" Recipe - Genius Kitchen", "")
        )

    def total_time(self):
        return get_minutes(self.soup.find("td", {"class": "time"}))

    def yields(self):
        return get_yields(
            self.soup.find("td", {"class": "servings"}).find("span", {"class": "count"})
        )

    def ingredients(self):
        ingredients = self.soup.find("ul", {"class": "ingredient-list"}).findAll("li")

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        raw_directions = (
            self.soup.find("div", {"class": "directions-inner container-xs"})
            .find("ol")
            .findAll("li")
        )

        directions = []

        for direction in raw_directions:
            if "Submit a Correction" not in direction.get_text():
                directions.append(normalize_string(direction.get_text()))

        return "\n".join(directions)

    def ratings(self):
        rating = self.soup.find("span", {"class": "sr-only"}).get_text()

        return round(float(rating), 2)
