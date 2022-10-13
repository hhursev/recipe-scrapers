# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._utils import normalize_string


class LeanAndGreenRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "leanandgreenrecipes.net"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        instructions = (
            self.soup.find("div", {"class": "item-list"}).find_next("ol").find_all("li")
        )
        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        cuisine = self.schema.cuisine()
        return cuisine[cuisine.find(">") + 1 :].replace("</a>", "")

    def description(self):
        return (
            self.schema.description()
            .replace("</p> <p>", "\n")
            .replace("<p>", "")
            .replace("</p>", "")
        )
