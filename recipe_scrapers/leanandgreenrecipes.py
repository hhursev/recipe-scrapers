# mypy: allow-untyped-defs

from bs4 import BeautifulSoup

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
        soup = BeautifulSoup(str(self.schema.cuisine()), features="html.parser")
        return soup.get_text()

    def description(self):
        descriptions = self.soup.find(
            "div", {"class": "block-field-blocknoderecipebody"}
        ).find_all("p")
        return "\n".join(
            [normalize_string(description.get_text()) for description in descriptions]
        )
