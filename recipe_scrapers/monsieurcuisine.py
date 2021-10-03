from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class MonsieurCuisine(AbstractScraper):
    @classmethod
    def host(cls):
        return "monsieur-cuisine.com"

    def author(self):
        container = self.soup.find("p", {"class": "recipe_author"})
        if not container:
            return None

        return container.span.get_text().strip()

    def title(self):
        return self.soup.h1.get_text()

    def total_time(self):
        container = self.soup.find("div", {"class": "duration-information"}).find(
            "div", {"class": "recipe-duration-total"}
        )
        if not container:
            return None

        minutes = get_minutes(container.b.get_text().replace(":", "h"))
        return minutes

    def yields(self):
        container = self.soup.find("div", {"class": "recipe--info"}).find(
            "div", {"class": "recipe-portions"}
        )
        if not container:
            return None

        return get_yields(container.get_text())

    def image(self):
        container = self.soup.find("meta", {"property": "og:image"})
        if not container:
            return None

        return container.get("content")

    def ingredients(self):
        container = self.soup.find(
            "div", {"class": "recipe--ingredients-html-item col-md-8"}
        )
        if not container:
            return None

        ingredients = container.findAll("li")

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        container = self.soup.find("div", {"class": "recipe--instructions"})
        if not container:
            return None

        instructions = container.find_all("li")

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def ratings(self):
        container = self.soup.find("div", {"class": "recipe--rating"})
        if not container:
            return None

        full_stars = container.find_all("span", {"class": "mc-star_filled"})
        half_stars = container.find_all("span", {"class": "mc-half_star_thick"})
        return len(full_stars) + 0.5 * len(half_stars)
