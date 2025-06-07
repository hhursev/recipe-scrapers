from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._utils import normalize_string
import re

destep_pattern = re.compile(r"^Step \d+\n")


def destep(line):
    return destep_pattern.sub("", line)


class Waitrose(AbstractScraper):
    @classmethod
    def host(cls):
        return "waitrose.com"

    def author(self):
        raise StaticValueException(return_value="Waitrose")

    def site_name(self):
        logo = next(iter(self.soup.select("div.logo")), None)
        if not logo:
            raise StaticValueException(return_value="Waitrose")
        if home_link := logo.find("a", {"href": "/"}):
            return home_link.text

    def image(self):
        img_tag = self.soup.find("img", {"itemprop": "image"})
        if img_tag:
            url = img_tag.get("src")
            return url[2:] if url.startswith("//") else url

    def ingredients(self):
        ingredient_items = self.soup.select("div[class^='ingredients'] li")
        if ingredient_items:
            ingredient_text = [
                normalize_string(item.get_text())
                for item in ingredient_items
                if item.get_text()
            ]
            return ingredient_text

    def instructions(self):
        instruction_items = self.soup.select("div[class^='method'] li")

        if instruction_items:
            instruction_text = [
                destep(normalize_string(item.get_text()))
                for item in instruction_items
                if item.get_text()
            ]
            return "\n".join(instruction_text)
