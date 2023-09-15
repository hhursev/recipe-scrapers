# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._utils import normalize_string


class GesundAktiv(AbstractScraper):
    @classmethod
    def host(cls):
        return "gesund-aktiv.com"

    def title(self):
        return self.soup.find("h1", {"class": "page-header"}).get_text()

    def image(self):
        return self.soup.find("a", {"class": "colorbox"})["href"]

    def ingredients(self):
        ingredients_container = self.soup.find(
            "div", {"class": "field--name-field-zutaten"}
        )
        ingredients = ingredients_container.findAll("div", {"class": "field--item"})
        return [normalize_string(instruction.get_text()) for instruction in ingredients]

    def instructions(self):
        instructions_container = self.soup.find(
            "div", {"class": "field--name-field-content-element"}
        )
        instructions = instructions_container.findAll("div", {"class": "field--item"})
        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def description(self):
        return normalize_string(
            self.soup.find("meta", {"name": "description"})["content"]
        )
