from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class WikiCookbook(AbstractScraper):
    @classmethod
    def host(cls):
        return "en.wikibooks.org"

    def title(self):
        return self.soup.find("h1").get_text().replace("Cookbook:", "")

    def total_time(self):
        return get_minutes(self.soup.find("th", string="Time").find_next_sibling("td"))

    def yields(self):
        return get_yields(
            self.soup.find("th", string="Servings").find_next_sibling("td")
        )

    def image(self):
        image = self.soup.find("a", {"class": "image"}).find("img", {"src": True})
        return image["src"] if image else None

    def ingredients(self):
        ingredients = (
            self.soup.find("span", {"id": "Ingredients"}).find_next("ul").findAll("li")
        )

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = (
            self.soup.find("span", {"id": "Procedure"}).find_next("ol").findAll("li")
        )

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
