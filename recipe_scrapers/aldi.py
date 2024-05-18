# mypy: allow-untyped-defs
import re

from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml
from ._utils import get_minutes, get_yields


class Aldi(AbstractScraper):
    @classmethod
    def host(cls):
        return "aldi.com.au"

    def site_name(self):
        return "Aldi"

    def author(self):
        return self.soup.find("meta", {"name": "author"}).get("content")

    def title(self):
        return self.soup.find("h1").text

    def category(self):
        title = self.soup.select("a.tab-nav--link.dropdown--list--link.m-active")[
            0
        ].text
        recipe_position = title.find(" Recipe")
        return title[:recipe_position]

    def prep_time(self):
        return get_minutes(self._get_value(re.compile("prep", re.IGNORECASE)))

    def cook_time(self):
        return get_minutes(self._get_value(re.compile("cook", re.IGNORECASE)))

    def total_time(self):
        total_time = 0

        try:
            total_time += self.prep_time()
        except ElementNotFoundInHtml:
            pass

        try:
            total_time += self.cook_time()
        except ElementNotFoundInHtml:
            pass

        return total_time

    def yields(self):
        value = self._get_value(re.compile("(makes)|(serves)", re.IGNORECASE))
        return get_yields(str(value))

    def image(self):
        figure = self.soup.find(
            "figure", {"class": "csc-textpic-image csc-textpic-last"}
        )
        if not figure:
            return None
        image = figure.find("img")
        if not image:
            return None
        return image.get("src")

    def ingredients(self):
        h2 = self.soup.find("h2", string=re.compile("Ingredients"))
        list_element = h2.find_next_sibling("ul")
        ingredients = []
        for li in list_element.find_all("li"):
            ingredients.append(li.text.strip())
        return ingredients

    def instructions(self):
        list_element = self.soup.find("ol")
        instructions = []
        for li in list_element.find_all("li"):
            instructions.append(li.text.strip())
        return "\n".join(instructions)

    def _get_value(self, label):
        label = self.soup.find("b", string=label)
        if not label:
            return None

        br_tags = label.find_next_siblings("br")

        parts = []
        for br in br_tags:
            next_sibling = br.next_sibling
            while next_sibling:
                text = next_sibling.text
                if text:
                    parts.append(text)
                next_sibling = next_sibling.next_sibling

        return " ".join(parts)
