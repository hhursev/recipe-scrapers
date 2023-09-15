# mypy: allow-untyped-defs

import re

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class Tofoo(AbstractScraper):
    @classmethod
    def host(cls):
        return "tofoo.co.uk"

    def author(self):
        return "The Tofoo co."

    def title(self):
        return self.soup.find(
            "h1", {"class": "recipe-detail__title h3 blue"}
        ).get_text()

    def category(self):
        category_text = self.soup.find(
            "div", {"class": "recipe-detail__ins h6"}
        ).get_text()
        normalized_category = normalize_string(category_text)
        return normalized_category

    def yields(self):
        desc = self.soup.find("div", {"class": "recipe-detail__desc"}).get_text()
        match = re.search(r"Serves (\d+)", desc)
        if match:
            return int(match.group(1))

    def total_time(self):
        desc = self.soup.find("div", {"class": "recipe-detail__desc"}).get_text()

        prep_time_match = re.search(r"Prep (\d+) min", desc)
        cooking_time_match = re.search(r"Cooking (\d+) min", desc)

        prep_time = int(prep_time_match.group(1)) if prep_time_match else 0
        cooking_time = int(cooking_time_match.group(1)) if cooking_time_match else 0

        return prep_time + cooking_time  # Return the summed time in minutes

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients_div = self.soup.find("div", {"class": "block-raw-material__body"})
        ingredients = [li.get_text() for li in ingredients_div.find_all("li")]
        return ingredients

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".block-raw-material h5",
            ".block-raw-material li",
        )

    def instructions(self):
        instructions_div = self.soup.find("div", {"class": "sect--do-this__title"})
        ol = instructions_div.find_next_sibling("ol")
        instructions = [li.get_text() for li in ol.find_all("li")]
        return "\n".join(instructions)
