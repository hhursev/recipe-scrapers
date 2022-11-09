# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._utils import normalize_string


class RosannaPansino(AbstractScraper):
    @classmethod
    def host(cls):
        return "rosannapansino.com"

    def title(self):
        return self.soup.find("meta", {"property": "og:title"})["content"]

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients = (
            self.soup.find("div", {"class": "recipe-left"})
            .find_next("em", string="Ingredients")
            .find_next_sibling("ul")
            .find_all("li")
        )
        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = (
            self.soup.find("div", {"class": "recipe-right"})
            .find_next("ol")
            .find_all("li")
        )
        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def description(self):
        descriptions = self.soup.find(
            "div", {"class": "recipe-main-image-caption"}
        ).find_all("p")
        return "\n".join(
            [normalize_string(description.get_text()) for description in descriptions]
        )
