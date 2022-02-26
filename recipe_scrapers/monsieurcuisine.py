from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class MonsieurCuisine(AbstractScraper):
    @classmethod
    def host(cls):
        return "monsieur-cuisine.com"

    def author(self):
        container = self.soup.find("p", {"class": "recipe_author"})

        return container.span.get_text().strip()

    def title(self):
        return self.soup.h1.get_text()

    def total_time(self):
        container = self.soup.find("div", {"class": "duration-information"}).find(
            "div", {"class": "recipe-duration-total"}
        )

        total_time = container.b.get_text()
        total_time_hours = total_time.split(":")[0]
        total_time_mins = total_time.split(":")[1]

        return get_minutes(f"{total_time_hours}h and {total_time_mins}mins")

    def yields(self):
        container = self.soup.find("div", {"class": "recipe--info"}).find(
            "div", {"class": "recipe-portions"}
        )

        return get_yields(container.get_text())

    def image(self):
        container = self.soup.find("div", {"class", "flexed-image-preview"})
        container = container.find("figure")
        container = container and container.find("img")
        if container and container.has_attr("src"):
            container = container["src"]

        if not container:
            return None

        return "https://www." + self.host() + container

    def ingredients(self):
        container = self.soup.find(
            "div", {"class": "recipe--ingredients-html-item col-md-8"}
        )

        ingredients = container.findAll("li")

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        container = self.soup.find("div", {"class": "recipe--instructions"})

        instructions = container.find_all("li")

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def ratings(self):
        container = self.soup.find("div", {"class": "recipe--rating"})

        full_stars = container.find_all("span", {"class": "mc-star_filled"})
        half_stars = container.find_all("span", {"class": "mc-half_star_thick"})
        return len(full_stars) + 0.5 * len(half_stars)
